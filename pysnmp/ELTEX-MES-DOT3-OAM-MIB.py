#
# PySNMP MIB module ELTEX-MES-DOT3-OAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-MES-DOT3-OAM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:46:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
elt_mes_mib_2, = mibBuilder.importSymbols("ELTEX-MES-MNG-MIB", "elt-mes-mib-2")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
iso, ObjectIdentity, ModuleIdentity, Integer32, NotificationType, Bits, IpAddress, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, Gauge32, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ObjectIdentity", "ModuleIdentity", "Integer32", "NotificationType", "Bits", "IpAddress", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "Gauge32", "MibIdentifier", "Counter32")
TruthValue, MacAddress, TimeStamp, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "MacAddress", "TimeStamp", "TextualConvention", "DisplayString")
eltMesDot3OamMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 1, 158))
eltMesDot3OamMIB.setRevisions(('2013-02-22 00:00', '2015-11-19 00:00',))
if mibBuilder.loadTexts: eltMesDot3OamMIB.setLastUpdated('201511190000Z')
if mibBuilder.loadTexts: eltMesDot3OamMIB.setOrganization('Eltex Ent')
eltMesDot3OamObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 1, 158, 1))
eltDot3OamClearStatistic = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 1, 158, 1, 7), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltDot3OamClearStatistic.setStatus('deprecated')
mibBuilder.exportSymbols("ELTEX-MES-DOT3-OAM-MIB", eltDot3OamClearStatistic=eltDot3OamClearStatistic, eltMesDot3OamMIB=eltMesDot3OamMIB, PYSNMP_MODULE_ID=eltMesDot3OamMIB, eltMesDot3OamObjects=eltMesDot3OamObjects)
