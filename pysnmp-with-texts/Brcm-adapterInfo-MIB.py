#
# PySNMP MIB module Brcm-adapterInfo-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Brcm-adapterInfo-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:42:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, TimeTicks, MibIdentifier, Counter32, IpAddress, Unsigned32, enterprises, Gauge32, ModuleIdentity, ObjectIdentity, Integer32, iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "MibIdentifier", "Counter32", "IpAddress", "Unsigned32", "enterprises", "Gauge32", "ModuleIdentity", "ObjectIdentity", "Integer32", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64")
DisplayString, TextualConvention, PhysAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "PhysAddress")
broadcom = MibIdentifier((1, 3, 6, 1, 4, 1, 4413))
enet = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1))
basp = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 2))
ifControllers = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 3))
baspConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 2, 1))
baspStat = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 2, 2))
baspTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 2, 3))
class InetAddressType(TextualConvention, Integer32):
    description = 'A value that represents a type of Internet address. unknown(0) An unknown address type. This value MUST be used if the value of the corresponding InetAddress object is a zero-length string. It may also be used to indicate an IP address that is not in one of the formats defined below. ipv4(1) An IPv4 address as defined by the InetAddressIPv4 textual convention. ipv6(2) An IPv6 address as defined by the InetAddressIPv6 textual convention. ipv4z(3) A non-global IPv4 address including a zone index as defined by the InetAddressIPv4z textual convention. ipv6z(4) A non-global IPv6 address including a zone index as defined by the InetAddressIPv6z textual convention. dns(16) A DNS domain name as defined by the InetAddressDNS textual convention. Each definition of a concrete InetAddressType value must be accompanied by a definition of a textual convention for use with that InetAddressType. To support future extensions, the InetAddressType textual convention SHOULD NOT be sub-typed in object type definitions. It MAY be sub-typed in compliance statements in order to require only a subset of these address types for a compliant implementation. Implementations must ensure that InetAddressType objects and any dependent objects (e.g., InetAddress objects) are consistent. An inconsistentValue error must be generated if an attempt to change an InetAddressType object would, for example, lead to an undefined InetAddress value. In particular, InetAddressType/InetAddress pairs must be changed together if the address type changes (e.g., from ipv6(2) to ipv4(1)).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 16))
    namedValues = NamedValues(("unknown", 0), ("ipv4", 1), ("ipv6", 2), ("ipv4z", 3), ("ipv6z", 4), ("dns", 16))

class InetAddress(TextualConvention, OctetString):
    description = "Denotes a generic Internet address. An InetAddress value is always interpreted within the context of an InetAddressType value. Every usage of the InetAddress textual convention is required to specify the InetAddressType object that provides the context. It is suggested that the InetAddressType object be logically registered before the object(s) that use the InetAddress textual convention, if they appear in the same logical row. The value of an InetAddress object must always be consistent with the value of the associated InetAddressType object. Attempts to set an InetAddress object to a value inconsistent with the associated InetAddressType must fail with an inconsistentValue error. When this textual convention is used as the syntax of an index object, there may be issues with the limit of 128 sub-identifiers specified in SMIv2, STD 58. In this case, the object definition MUST include a 'SIZE' clause to limit the number of potential instance sub-identifiers; otherwise the applicable constraints MUST be stated in the appropriate conceptual row DESCRIPTION clauses, or in the surrounding documentation if there is no single DESCRIPTION clause that is appropriate."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class InetAddressIPv4(TextualConvention, OctetString):
    description = 'Represents an IPv4 network address: Octets Contents Encoding 1-4 IPv4 address network-byte order The corresponding InetAddressType value is ipv4(1). This textual convention SHOULD NOT be used directly in object definitions, as it restricts addresses to a specific format. However, if it is used, it MAY be used either on its own or in conjunction with InetAddressType, as a pair.'
    status = 'current'
    displayHint = '1d.1d.1d.1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class InetAddressIPv6(TextualConvention, OctetString):
    description = 'Represents an IPv6 network address: Octets Contents Encoding 1-16 IPv6 address network-byte order The corresponding InetAddressType value is ipv6(2). This textual convention SHOULD NOT be used directly in object definitions, as it restricts addresses to a specific format. However, if it is used, it MAY be used either on its own or in conjunction with InetAddressType, as a pair.'
    status = 'current'
    displayHint = '2x:2x:2x:2x:2x:2x:2x:2x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(16, 16)
    fixedLength = 16

ifNumber = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifNumber.setStatus('mandatory')
if mibBuilder.loadTexts: ifNumber.setDescription('The number of Broadcom network interfaces (regardless of their current state) present on this system.')
ifTable = MibTable((1, 3, 6, 1, 4, 1, 4413, 1, 3, 2), )
if mibBuilder.loadTexts: ifTable.setStatus('mandatory')
if mibBuilder.loadTexts: ifTable.setDescription('A list of Broadcom network interface entries. The number of entries is given by the ifNumber.')
ifEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4413, 1, 3, 2, 1), ).setIndexNames((0, "Brcm-adapterInfo-MIB", "ifIndex"))
if mibBuilder.loadTexts: ifEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ifEntry.setDescription('An entry containing statistics objects of a Broadcom network interface in this system.')
ifIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ifIndex.setDescription("An unique value for each Broadcom interface. The value for each interface must remain constant at least from one re-initialization of the entity's network management system to the next re- initialization.")
ifName = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 3, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifName.setStatus('mandatory')
if mibBuilder.loadTexts: ifName.setDescription(' A textual string containing name of the adapter or team')
ifDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 3, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifDescr.setStatus('mandatory')
if mibBuilder.loadTexts: ifDescr.setDescription(' A textual string containing the adapter or team description')
ifNetworkAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 3, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifNetworkAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ifNetworkAddress.setDescription('IP address of the adapter.')
ifSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 3, 2, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifSubnetMask.setStatus('mandatory')
if mibBuilder.loadTexts: ifSubnetMask.setDescription('IP subnet Mask of the adapter.')
ifPhysAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 3, 2, 1, 6), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifPhysAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ifPhysAddress.setDescription('MAC address of the adapter.')
ifPermPhysAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 3, 2, 1, 7), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifPermPhysAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ifPermPhysAddress.setDescription('Permanent MAC address of the adapter.')
ifLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 3, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("link-up", 1), ("link-fail", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifLinkStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ifLinkStatus.setDescription(' Adapter link status, this information only applicable to the Broadcom adapter')
ifState = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 3, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("normal-mode", 1), ("diagnotic-mode", 2), ("adapter-removed", 3), ("lowpower-mode", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifState.setStatus('mandatory')
if mibBuilder.loadTexts: ifState.setDescription('The operating mode of the driver, this information only applicable to the Broadcom adapter')
ifLineSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 3, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unknown", 1), ("speed-10-Mbps", 2), ("speed-100-Mbps", 3), ("speed-1000-Mbps", 4), ("speed-2500-Mbps", 5), ("speed-10-Gbps", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifLineSpeed.setStatus('mandatory')
if mibBuilder.loadTexts: ifLineSpeed.setDescription(' The operating speed of the adapter, this information only applicable to the Broadcom adapter')
ifDuplexMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 3, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("half-duplex", 2), ("full-duplex", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifDuplexMode.setStatus('mandatory')
if mibBuilder.loadTexts: ifDuplexMode.setDescription(' Adapter duplex mode, this information only applicable to the Broadcom adapter')
ifMemBaseLow = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 3, 2, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifMemBaseLow.setStatus('mandatory')
if mibBuilder.loadTexts: ifMemBaseLow.setDescription(' memory low range of the adapter, this information only applicable to the Broadcom adapter')
ifMemBaseHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 3, 2, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifMemBaseHigh.setStatus('mandatory')
if mibBuilder.loadTexts: ifMemBaseHigh.setDescription(' memory high range of the adapter, this information only applicable to the Broadcom adapter')
ifInterrupt = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 3, 2, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifInterrupt.setStatus('mandatory')
if mibBuilder.loadTexts: ifInterrupt.setDescription(' IRQ value for the adapter, this information only applicable to the Broadcom adapter')
ifBusNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 3, 2, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifBusNumber.setStatus('mandatory')
if mibBuilder.loadTexts: ifBusNumber.setDescription(' PCI Bus Number where the Adapter is situated, this information only applicable to the Broadcom adapter')
ifDeviceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 3, 2, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifDeviceNumber.setStatus('mandatory')
if mibBuilder.loadTexts: ifDeviceNumber.setDescription(' PCI Device Number of the adapter, this information only applicable to the Broadcom adapter')
ifFunctionNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 3, 2, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifFunctionNumber.setStatus('mandatory')
if mibBuilder.loadTexts: ifFunctionNumber.setDescription(' PCI Function Number of the adapter, this information only applicable to the Broadcom adapter')
ifIpv6NetworkAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 3, 2, 1, 18), InetAddressIPv6()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifIpv6NetworkAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ifIpv6NetworkAddress.setDescription('IPv6 address of the adapter.')
mibBuilder.exportSymbols("Brcm-adapterInfo-MIB", InetAddressIPv4=InetAddressIPv4, baspTrap=baspTrap, ifState=ifState, ifFunctionNumber=ifFunctionNumber, ifName=ifName, ifBusNumber=ifBusNumber, ifEntry=ifEntry, ifPhysAddress=ifPhysAddress, baspStat=baspStat, ifMemBaseLow=ifMemBaseLow, ifNetworkAddress=ifNetworkAddress, ifDuplexMode=ifDuplexMode, ifLineSpeed=ifLineSpeed, ifSubnetMask=ifSubnetMask, ifNumber=ifNumber, ifControllers=ifControllers, ifIndex=ifIndex, ifDescr=ifDescr, broadcom=broadcom, ifPermPhysAddress=ifPermPhysAddress, ifInterrupt=ifInterrupt, InetAddressType=InetAddressType, baspConfig=baspConfig, ifTable=ifTable, ifLinkStatus=ifLinkStatus, basp=basp, InetAddress=InetAddress, InetAddressIPv6=InetAddressIPv6, ifIpv6NetworkAddress=ifIpv6NetworkAddress, ifMemBaseHigh=ifMemBaseHigh, ifDeviceNumber=ifDeviceNumber, enet=enet)
