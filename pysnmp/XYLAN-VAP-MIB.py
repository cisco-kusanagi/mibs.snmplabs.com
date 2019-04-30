#
# PySNMP MIB module XYLAN-VAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XYLAN-VAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:39:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
MacAddress, = mibBuilder.importSymbols("BRIDGE-MIB", "MacAddress")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Unsigned32, iso, TimeTicks, Bits, NotificationType, Gauge32, MibIdentifier, Integer32, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Unsigned32", "iso", "TimeTicks", "Bits", "NotificationType", "Gauge32", "MibIdentifier", "Integer32", "Counter64", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
xylanVapArch, = mibBuilder.importSymbols("XYLAN-BASE-MIB", "xylanVapArch")
xVapInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 800, 2, 10, 1))
class XylanVapAdminStatCodes(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("disable", 1), ("enable", 2), ("partial", 3))

xVapAdmStatus = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 10, 1, 1), XylanVapAdminStatCodes()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xVapAdmStatus.setStatus('mandatory')
xVapTable = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 10, 1, 2), )
if mibBuilder.loadTexts: xVapTable.setStatus('mandatory')
xVapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 10, 1, 2, 1), ).setIndexNames((0, "XYLAN-VAP-MIB", "xVapMACAddress"), (0, "XYLAN-VAP-MIB", "xVapSlot"), (0, "XYLAN-VAP-MIB", "xVapPort"))
if mibBuilder.loadTexts: xVapEntry.setStatus('mandatory')
xVapPrimaryAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 10, 1, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xVapPrimaryAddress.setStatus('mandatory')
xVapSecondaryAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 10, 1, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xVapSecondaryAddress.setStatus('mandatory')
xVapSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 10, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xVapSlot.setStatus('mandatory')
xVapPort = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 10, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xVapPort.setStatus('mandatory')
xVapMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 10, 1, 2, 1, 5), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xVapMACAddress.setStatus('mandatory')
xVapGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 10, 1, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xVapGroupId.setStatus('mandatory')
mibBuilder.exportSymbols("XYLAN-VAP-MIB", xVapSecondaryAddress=xVapSecondaryAddress, xVapEntry=xVapEntry, xVapInfo=xVapInfo, xVapGroupId=xVapGroupId, XylanVapAdminStatCodes=XylanVapAdminStatCodes, xVapAdmStatus=xVapAdmStatus, xVapMACAddress=xVapMACAddress, xVapSlot=xVapSlot, xVapTable=xVapTable, xVapPort=xVapPort, xVapPrimaryAddress=xVapPrimaryAddress)
