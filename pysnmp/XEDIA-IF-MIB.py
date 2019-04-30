#
# PySNMP MIB module XEDIA-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XEDIA-IF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:36:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
InterfaceIndex, ifIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex", "InterfaceIndexOrZero")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ObjectIdentity, Bits, TimeTicks, Gauge32, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter64, MibIdentifier, Integer32, ModuleIdentity, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Bits", "TimeTicks", "Gauge32", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter64", "MibIdentifier", "Integer32", "ModuleIdentity", "Counter32", "iso")
DisplayString, RowStatus, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TruthValue", "TextualConvention")
xediaMibs, = mibBuilder.importSymbols("XEDIA-REG", "xediaMibs")
xediaIfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 838, 3, 40))
if mibBuilder.loadTexts: xediaIfMIB.setLastUpdated('9911112155Z')
if mibBuilder.loadTexts: xediaIfMIB.setOrganization('Xedia Corp.')
xifObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 40, 1))
xifNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 40, 2))
xifConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 40, 3))
class Unsigned32(Gauge32):
    pass

xifNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 838, 3, 40, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xifNextIndex.setStatus('current')
xifTable = MibTable((1, 3, 6, 1, 4, 1, 838, 3, 40, 1, 2), )
if mibBuilder.loadTexts: xifTable.setStatus('current')
xifEntry = MibTableRow((1, 3, 6, 1, 4, 1, 838, 3, 40, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: xifEntry.setStatus('current')
xifRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 40, 1, 2, 1, 1), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xifRowStatus.setStatus('current')
mibBuilder.exportSymbols("XEDIA-IF-MIB", xifRowStatus=xifRowStatus, Unsigned32=Unsigned32, xifObjects=xifObjects, xifTable=xifTable, xifNextIndex=xifNextIndex, xediaIfMIB=xediaIfMIB, PYSNMP_MODULE_ID=xediaIfMIB, xifNotifications=xifNotifications, xifEntry=xifEntry, xifConformance=xifConformance)
