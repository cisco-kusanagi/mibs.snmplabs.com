#
# PySNMP MIB module ELTEX-DOT3-OAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-DOT3-OAM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:00:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
eltexLtd, = mibBuilder.importSymbols("ELTEX-SMI-ACTUAL", "eltexLtd")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, iso, NotificationType, ObjectIdentity, Counter64, TimeTicks, IpAddress, MibIdentifier, Integer32, ModuleIdentity, Unsigned32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "iso", "NotificationType", "ObjectIdentity", "Counter64", "TimeTicks", "IpAddress", "MibIdentifier", "Integer32", "ModuleIdentity", "Unsigned32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TruthValue, TimeStamp, MacAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TimeStamp", "MacAddress", "TextualConvention", "DisplayString")
eltexDot3OamMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 30))
eltexDot3OamMIB.setRevisions(('2013-02-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: eltexDot3OamMIB.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: eltexDot3OamMIB.setLastUpdated('201302220000Z')
if mibBuilder.loadTexts: eltexDot3OamMIB.setOrganization('Eltex Ent')
if mibBuilder.loadTexts: eltexDot3OamMIB.setContactInfo('www.eltex.nsk.ru')
if mibBuilder.loadTexts: eltexDot3OamMIB.setDescription('Initial version.')
eltexDot3OamObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 30, 1))
eltexDot3OamClearStatistic = MibScalar((1, 3, 6, 1, 4, 1, 35265, 30, 1, 7), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltexDot3OamClearStatistic.setStatus('current')
if mibBuilder.loadTexts: eltexDot3OamClearStatistic.setDescription('Each bit that is set in this portList represent a port that its OAM statistic should be reset.')
mibBuilder.exportSymbols("ELTEX-DOT3-OAM-MIB", eltexDot3OamObjects=eltexDot3OamObjects, eltexDot3OamMIB=eltexDot3OamMIB, eltexDot3OamClearStatistic=eltexDot3OamClearStatistic, PYSNMP_MODULE_ID=eltexDot3OamMIB)
