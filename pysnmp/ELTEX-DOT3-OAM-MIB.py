#
# PySNMP MIB module ELTEX-DOT3-OAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-DOT3-OAM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:45:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
eltexLtd, = mibBuilder.importSymbols("ELTEX-SMI-ACTUAL", "eltexLtd")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Gauge32, Unsigned32, Integer32, Counter32, Bits, ModuleIdentity, MibIdentifier, IpAddress, TimeTicks, Counter64, iso, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Unsigned32", "Integer32", "Counter32", "Bits", "ModuleIdentity", "MibIdentifier", "IpAddress", "TimeTicks", "Counter64", "iso", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType")
DisplayString, MacAddress, TruthValue, TextualConvention, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TruthValue", "TextualConvention", "TimeStamp")
eltexDot3OamMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 30))
eltexDot3OamMIB.setRevisions(('2013-02-22 00:00',))
if mibBuilder.loadTexts: eltexDot3OamMIB.setLastUpdated('201302220000Z')
if mibBuilder.loadTexts: eltexDot3OamMIB.setOrganization('Eltex Ent')
eltexDot3OamObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 30, 1))
eltexDot3OamClearStatistic = MibScalar((1, 3, 6, 1, 4, 1, 35265, 30, 1, 7), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltexDot3OamClearStatistic.setStatus('current')
mibBuilder.exportSymbols("ELTEX-DOT3-OAM-MIB", eltexDot3OamMIB=eltexDot3OamMIB, eltexDot3OamClearStatistic=eltexDot3OamClearStatistic, eltexDot3OamObjects=eltexDot3OamObjects, PYSNMP_MODULE_ID=eltexDot3OamMIB)
