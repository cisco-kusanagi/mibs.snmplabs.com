#
# PySNMP MIB module CT-DAREGISTRY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CT-DAREGISTRY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:12:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
cabletron, = mibBuilder.importSymbols("CTRON-OIDS", "cabletron")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, iso, Counter64, ModuleIdentity, Integer32, Bits, NotificationType, Gauge32, MibIdentifier, IpAddress, ObjectIdentity, Unsigned32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "Counter64", "ModuleIdentity", "Integer32", "Bits", "NotificationType", "Gauge32", "MibIdentifier", "IpAddress", "ObjectIdentity", "Unsigned32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ctSSA = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4497))
class DisplayString(OctetString):
    pass

ctDARegistryTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4497, 1), )
if mibBuilder.loadTexts: ctDARegistryTable.setStatus('mandatory')
ctDARegistryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4497, 1, 1), ).setIndexNames((0, "CT-DAREGISTRY-MIB", "ctDARegistryIndex"), (0, "CT-DAREGISTRY-MIB", "ctDARegistryInstance"))
if mibBuilder.loadTexts: ctDARegistryEntry.setStatus('mandatory')
ctDARegistryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDARegistryIndex.setStatus('mandatory')
ctDARegistryInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDARegistryInstance.setStatus('mandatory')
ctDARegistryAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDARegistryAdminStatus.setStatus('mandatory')
ctDARegistryOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3), ("unknown", 4), ("dormant", 5), ("notPresent", 6), ("lowerLayerDown", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDARegistryOperStatus.setStatus('mandatory')
ctDARegistryLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 1, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDARegistryLastChange.setStatus('mandatory')
ctDARegistryDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDARegistryDescr.setStatus('mandatory')
mibBuilder.exportSymbols("CT-DAREGISTRY-MIB", ctDARegistryTable=ctDARegistryTable, ctSSA=ctSSA, ctDARegistryLastChange=ctDARegistryLastChange, ctDARegistryIndex=ctDARegistryIndex, ctDARegistryOperStatus=ctDARegistryOperStatus, DisplayString=DisplayString, ctDARegistryEntry=ctDARegistryEntry, ctDARegistryAdminStatus=ctDARegistryAdminStatus, ctDARegistryDescr=ctDARegistryDescr, ctDARegistryInstance=ctDARegistryInstance)
