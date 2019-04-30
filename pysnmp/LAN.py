#
# PySNMP MIB module LAN (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LAN
# Produced by pysmi-0.3.4 at Mon Apr 29 19:54:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter32, Gauge32, enterprises, TimeTicks, Bits, NotificationType, Counter64, MibIdentifier, iso, IpAddress, ObjectIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Gauge32", "enterprises", "TimeTicks", "Bits", "NotificationType", "Counter64", "MibIdentifier", "iso", "IpAddress", "ObjectIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ModuleIdentity")
TruthValue, RowStatus, TextualConvention, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "TextualConvention", "MacAddress", "DisplayString")
pepwave = MibIdentifier((1, 3, 6, 1, 4, 1, 27662))
productMib = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 200))
generalMib = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 200, 1))
lanMib = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 200, 1, 3))
lanInfo = ModuleIdentity((1, 3, 6, 1, 4, 1, 27662, 200, 1, 3, 1))
if mibBuilder.loadTexts: lanInfo.setLastUpdated('201305220000Z')
if mibBuilder.loadTexts: lanInfo.setOrganization('PEPWAVE')
class PortSpeedType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("unknown", 0), ("auto", 1), ("fullDulplex10", 2), ("halfDulplex10", 3), ("fullDulplex100", 4), ("halfDulplex100", 5), ("fullDulplex1000", 6), ("halfDulplex1000", 7))

lanStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 200, 1, 3, 1, 1))
lanIp = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 3, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lanIp.setStatus('current')
lanSubnetMask = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 3, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lanSubnetMask.setStatus('current')
lanSpeed = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 3, 1, 1, 3), PortSpeedType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lanSpeed.setStatus('current')
mibBuilder.exportSymbols("LAN", lanIp=lanIp, PYSNMP_MODULE_ID=lanInfo, lanInfo=lanInfo, productMib=productMib, lanStatus=lanStatus, lanSpeed=lanSpeed, PortSpeedType=PortSpeedType, generalMib=generalMib, lanMib=lanMib, pepwave=pepwave, lanSubnetMask=lanSubnetMask)
