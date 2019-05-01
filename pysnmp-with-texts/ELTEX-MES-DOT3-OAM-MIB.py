#
# PySNMP MIB module ELTEX-MES-DOT3-OAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-MES-DOT3-OAM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:01:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
elt_mes_mib_2, = mibBuilder.importSymbols("ELTEX-MES-MNG-MIB", "elt-mes-mib-2")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Integer32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, Bits, MibIdentifier, TimeTicks, ObjectIdentity, IpAddress, ModuleIdentity, Counter64, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "Bits", "MibIdentifier", "TimeTicks", "ObjectIdentity", "IpAddress", "ModuleIdentity", "Counter64", "Gauge32", "iso")
TruthValue, TimeStamp, DisplayString, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TimeStamp", "DisplayString", "MacAddress", "TextualConvention")
eltMesDot3OamMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 1, 158))
eltMesDot3OamMIB.setRevisions(('2013-02-22 00:00', '2015-11-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: eltMesDot3OamMIB.setRevisionsDescriptions(('Initial revision.', 'Deprecate all objects in this module.',))
if mibBuilder.loadTexts: eltMesDot3OamMIB.setLastUpdated('201511190000Z')
if mibBuilder.loadTexts: eltMesDot3OamMIB.setOrganization('Eltex Ent')
if mibBuilder.loadTexts: eltMesDot3OamMIB.setContactInfo('www.eltex.nsk.ru')
if mibBuilder.loadTexts: eltMesDot3OamMIB.setDescription('Initial version.')
eltMesDot3OamObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 1, 158, 1))
eltDot3OamClearStatistic = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 1, 158, 1, 7), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltDot3OamClearStatistic.setStatus('deprecated')
if mibBuilder.loadTexts: eltDot3OamClearStatistic.setDescription('Each bit that is set in this portList represent a port that its OAM statistic should be reset.')
mibBuilder.exportSymbols("ELTEX-MES-DOT3-OAM-MIB", eltMesDot3OamMIB=eltMesDot3OamMIB, eltMesDot3OamObjects=eltMesDot3OamObjects, PYSNMP_MODULE_ID=eltMesDot3OamMIB, eltDot3OamClearStatistic=eltDot3OamClearStatistic)
