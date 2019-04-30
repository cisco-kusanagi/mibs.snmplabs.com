#
# PySNMP MIB module Brcm-adapterInfo-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Brcm-adapterInfo-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:25:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, TimeTicks, Integer32, NotificationType, Counter64, MibIdentifier, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Gauge32, ModuleIdentity, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "TimeTicks", "Integer32", "NotificationType", "Counter64", "MibIdentifier", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Gauge32", "ModuleIdentity", "enterprises")
PhysAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "PhysAddress", "DisplayString", "TextualConvention")
broadcom = MibIdentifier((1, 3, 6, 1, 4, 1, 4413))
enet = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1))
basp = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 2))
ifControllers = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 3))
baspConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 2, 1))
baspStat = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 2, 2))
baspTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 2, 3))
class InetAddressType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 16))
    namedValues = NamedValues(("unknown", 0), ("ipv4", 1), ("ipv6", 2), ("ipv4z", 3), ("ipv6z", 4), ("dns", 16))

class InetAddress(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class InetAddressIPv4(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1d.1d.1d.1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class InetAddressIPv6(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2x:2x:2x:2x:2x:2x:2x:2x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(16, 16)
    fixedLength = 16

ifNumber = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifNumber.setStatus('mandatory')
ifTable = MibTable((1, 3, 6, 1, 4, 1, 4413, 1, 3, 2), )
if mibBuilder.loadTexts: ifTable.setStatus('mandatory')
ifEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4413, 1, 3, 2, 1), ).setIndexNames((0, "Brcm-adapterInfo-MIB", "ifIndex"))
if mibBuilder.loadTexts: ifEntry.setStatus('mandatory')
ifIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifIndex.setStatus('mandatory')
ifName = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 3, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifName.setStatus('mandatory')
ifDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 3, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifDescr.setStatus('mandatory')
ifNetworkAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 3, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifNetworkAddress.setStatus('mandatory')
ifSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 3, 2, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifSubnetMask.setStatus('mandatory')
ifPhysAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 3, 2, 1, 6), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifPhysAddress.setStatus('mandatory')
ifPermPhysAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 3, 2, 1, 7), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifPermPhysAddress.setStatus('mandatory')
ifLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 3, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("link-up", 1), ("link-fail", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifLinkStatus.setStatus('mandatory')
ifState = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 3, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("normal-mode", 1), ("diagnotic-mode", 2), ("adapter-removed", 3), ("lowpower-mode", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifState.setStatus('mandatory')
ifLineSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 3, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unknown", 1), ("speed-10-Mbps", 2), ("speed-100-Mbps", 3), ("speed-1000-Mbps", 4), ("speed-2500-Mbps", 5), ("speed-10-Gbps", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifLineSpeed.setStatus('mandatory')
ifDuplexMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 3, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("half-duplex", 2), ("full-duplex", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifDuplexMode.setStatus('mandatory')
ifMemBaseLow = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 3, 2, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifMemBaseLow.setStatus('mandatory')
ifMemBaseHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 3, 2, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifMemBaseHigh.setStatus('mandatory')
ifInterrupt = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 3, 2, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifInterrupt.setStatus('mandatory')
ifBusNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 3, 2, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifBusNumber.setStatus('mandatory')
ifDeviceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 3, 2, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifDeviceNumber.setStatus('mandatory')
ifFunctionNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 3, 2, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifFunctionNumber.setStatus('mandatory')
ifIpv6NetworkAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 3, 2, 1, 18), InetAddressIPv6()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifIpv6NetworkAddress.setStatus('mandatory')
mibBuilder.exportSymbols("Brcm-adapterInfo-MIB", ifLinkStatus=ifLinkStatus, ifSubnetMask=ifSubnetMask, baspConfig=baspConfig, ifIpv6NetworkAddress=ifIpv6NetworkAddress, ifPhysAddress=ifPhysAddress, baspStat=baspStat, broadcom=broadcom, InetAddressIPv4=InetAddressIPv4, enet=enet, ifEntry=ifEntry, ifDeviceNumber=ifDeviceNumber, ifBusNumber=ifBusNumber, ifPermPhysAddress=ifPermPhysAddress, InetAddress=InetAddress, InetAddressType=InetAddressType, baspTrap=baspTrap, ifMemBaseHigh=ifMemBaseHigh, ifControllers=ifControllers, ifNetworkAddress=ifNetworkAddress, ifDuplexMode=ifDuplexMode, ifFunctionNumber=ifFunctionNumber, ifIndex=ifIndex, InetAddressIPv6=InetAddressIPv6, ifLineSpeed=ifLineSpeed, ifNumber=ifNumber, ifTable=ifTable, ifInterrupt=ifInterrupt, ifName=ifName, ifMemBaseLow=ifMemBaseLow, basp=basp, ifState=ifState, ifDescr=ifDescr)
