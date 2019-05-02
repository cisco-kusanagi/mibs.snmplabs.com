#
# PySNMP MIB module LAN (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LAN
# Produced by pysmi-0.3.4 at Wed May  1 14:05:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ModuleIdentity, Gauge32, TimeTicks, Counter64, MibIdentifier, NotificationType, Bits, Integer32, iso, ObjectIdentity, IpAddress, Unsigned32, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Gauge32", "TimeTicks", "Counter64", "MibIdentifier", "NotificationType", "Bits", "Integer32", "iso", "ObjectIdentity", "IpAddress", "Unsigned32", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32")
MacAddress, DisplayString, TextualConvention, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DisplayString", "TextualConvention", "RowStatus", "TruthValue")
pepwave = MibIdentifier((1, 3, 6, 1, 4, 1, 27662))
productMib = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 200))
generalMib = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 200, 1))
lanMib = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 200, 1, 3))
lanInfo = ModuleIdentity((1, 3, 6, 1, 4, 1, 27662, 200, 1, 3, 1))
if mibBuilder.loadTexts: lanInfo.setLastUpdated('201305220000Z')
if mibBuilder.loadTexts: lanInfo.setOrganization('PEPWAVE')
if mibBuilder.loadTexts: lanInfo.setContactInfo('')
if mibBuilder.loadTexts: lanInfo.setDescription('MIB module for LAN.')
class PortSpeedType(TextualConvention, Integer32):
    description = 'Describe the port speed and type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("unknown", 0), ("auto", 1), ("fullDulplex10", 2), ("halfDulplex10", 3), ("fullDulplex100", 4), ("halfDulplex100", 5), ("fullDulplex1000", 6), ("halfDulplex1000", 7))

lanStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 200, 1, 3, 1, 1))
lanIp = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 3, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lanIp.setStatus('current')
if mibBuilder.loadTexts: lanIp.setDescription('LAN IP address.')
lanSubnetMask = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 3, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lanSubnetMask.setStatus('current')
if mibBuilder.loadTexts: lanSubnetMask.setDescription('LAN subnet mask.')
lanSpeed = MibScalar((1, 3, 6, 1, 4, 1, 27662, 200, 1, 3, 1, 1, 3), PortSpeedType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lanSpeed.setStatus('current')
if mibBuilder.loadTexts: lanSpeed.setDescription('LAN speed status (Auto/10baseT-FD/ 10baseT-HD/100baseTx-FD/100baseTx-HD/1000baseTx-FD/ 1000baseTx-HD.')
mibBuilder.exportSymbols("LAN", pepwave=pepwave, PYSNMP_MODULE_ID=lanInfo, lanStatus=lanStatus, lanInfo=lanInfo, lanIp=lanIp, lanSpeed=lanSpeed, lanMib=lanMib, PortSpeedType=PortSpeedType, generalMib=generalMib, productMib=productMib, lanSubnetMask=lanSubnetMask)
