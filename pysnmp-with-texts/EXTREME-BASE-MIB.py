#
# PySNMP MIB module EXTREME-BASE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EXTREME-BASE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:07:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Counter64, IpAddress, Integer32, Gauge32, Counter32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, ModuleIdentity, ObjectIdentity, enterprises, TimeTicks, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "IpAddress", "Integer32", "Gauge32", "Counter32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "ModuleIdentity", "ObjectIdentity", "enterprises", "TimeTicks", "Bits", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
extremenetworks = MibIdentifier((1, 3, 6, 1, 4, 1, 1916))
extremeV1Traps = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 0))
extremeAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1))
extremeProduct = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 2))
extremeMisc = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 3))
extremeV2Traps = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 4))
summit1 = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 2, 1))
summit2 = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 2, 2))
summit3 = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 2, 3))
summit4 = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 2, 4))
summit4fx = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 2, 5))
summit48 = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 2, 6))
summit24 = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 2, 7))
blackDiamond6800 = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 2, 8))
blackDiamond6808 = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 2, 11))
summit7iSX = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 2, 12))
summit7iTX = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 2, 13))
summit1iTX = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 2, 14))
summit5i = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 2, 15))
summit48i = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 2, 16))
alpine3808 = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 2, 17))
summit1iSX = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 2, 19))
alpine3804 = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 2, 20))
summit5iLX = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 2, 21))
summit5iTX = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 2, 22))
enetSwitch24Port = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 2, 23))
blackDiamond6816 = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 2, 24))
summit24e3 = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 2, 25))
alpine3802 = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 2, 26))
blackDiamond6804 = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 2, 27))
summit48si = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 2, 28))
summitPx1 = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 2, 30))
summit24e2TX = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 2, 40))
summit24e2SX = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 2, 41))
summit200_24 = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 2, 53)).setLabel("summit200-24")
summit200_48 = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 2, 54)).setLabel("summit200-48")
summit400_48t = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 2, 58)).setLabel("summit400-48t")
summit400_24x = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 2, 59)).setLabel("summit400-24x")
summit400_24t = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 2, 63)).setLabel("summit400-24t")
summit400_24p = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 2, 64)).setLabel("summit400-24p")
summit300_24 = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 2, 61)).setLabel("summit300-24")
summit300_48 = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 2, 55)).setLabel("summit300-48")
extremeStack = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 2, 67))
summit200_24fx = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 2, 70)).setLabel("summit200-24fx")
extremeOids = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 3, 1))
extremeMauType = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 3, 1, 1))
extremeMauType1000BaseSX = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 1))
extremeMauType1000BaseLX = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 2))
extremeMauType1000BaseCX = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 3))
extremeMauType1000BaseSXFD = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 4))
extremeMauType1000BaseLXFD = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 5))
extremeMauType1000BaseCXFD = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 6))
extremeMauType1000BaseWDMHD = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 7))
extremeMauType1000BaseWDMFD = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 8))
extremeMauType1000BaseLX70HD = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 9))
extremeMauType1000BaseLX70FD = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 10))
extremeMauType1000BaseZXHD = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 11))
extremeMauType1000BaseZXFD = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 12))
extremeMauType1000BaseLX100HD = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 13))
extremeMauType1000BaseLX100FD = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 3, 1, 1, 14))
extremeSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 1))
extremeVlan = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 2))
extremeQos = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 3))
extremePort = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 4))
extremeVC = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 5))
extremeTrapPoll = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 6))
extremeQosPolicy = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 7))
extremeDlcs = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 8))
extremeFileTransfer = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 10))
extremeRtStats = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 11))
extremeEsrp = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 12))
extremeEdp = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 13))
extremeSlb = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 14))
extremeOspf = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 15))
extremeFdb = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 16))
extremeStp = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 17))
extremePOSMib = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 20))
extremeNPMib = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 21))
extremeNetFlow = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 22))
extremeSnmpv3 = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 23))
extremeCable = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 24))
extremeDosMib = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 28))
extremeEnhDosMib = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 29))
extremeWireless = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 25))
extremeEntity = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 31))
extremeAP = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 25, 1))
extremeLAC = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 25, 2))
class PortList(TextualConvention, OctetString):
    description = "Each octet within this value specifies a set of eight ports, with the first octet specifying ports 1 through 8, the second octet specifying ports 9 through 16, etc. Within each octet, the most significant bit represents the lowest numbered port, and the least significant bit represents the highest numbered port. Thus, each port of the bridge is represented by a single bit within the value of this object. If that bit has a value of '1' then that port is included in the set of ports; the port is not included if its bit has a value of '0'. If the object has a length of 0 then it is taken to refer to all of the ports in a given device."
    status = 'current'

class L4Port(TextualConvention, Integer32):
    description = 'The value of a transport layer (layer-4) port number, in network byte order. A value of 0 indicates all allowed values of this field i.e. wildcard.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 65535), )
class ExtremeGenAddr(TextualConvention, OctetString):
    description = 'The value of an address.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 20)

class ExtremeDeviceId(TextualConvention, OctetString):
    description = 'The switch identifier used by Extreme EDP protocol.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class WPACipherSet(TextualConvention, Bits):
    description = 'A set of supported ciphers which can be advertised by WPA stations. Each set bit indicates support for a given cipher suite. The special value none is allowed for representing the absence of information. The value other is used to indicate an unknown cipher.'
    status = 'current'
    namedValues = NamedValues(("none", 0), ("wep64", 1), ("tkip", 2), ("wrap", 3), ("ccmp", 4), ("wep128", 5), ("other", 6))

class WPAKeyMgmtSet(TextualConvention, Bits):
    description = 'A set of supported key management suites. For more info see IEEE 802.11i D3.0 section 7.'
    status = 'current'
    namedValues = NamedValues(("none", 0), ("dot1x", 1), ("psk", 2))

class ClientAuthType(TextualConvention, Integer32):
    description = 'Type of client specified in the netlogin traps as well as the client table. For wired clients, only none, netlogin and dot1x are valid'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("none", 0), ("open", 1), ("wep", 2), ("mac-based", 3), ("dot1x", 4), ("wpa-psk", 5), ("web-based", 6), ("wpa", 7), ("wpa2", 8), ("wpa2-psk", 9))

class WirelessRemoteConnectBindingType(TextualConvention, Integer32):
    description = 'The type of binding to be used when mapping APs to virtual ports'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("mac-address", 1), ("serial-number", 2), ("ip-address", 3))

mibBuilder.exportSymbols("EXTREME-BASE-MIB", extremeNetFlow=extremeNetFlow, extremeV2Traps=extremeV2Traps, extremeDlcs=extremeDlcs, extremeSlb=extremeSlb, ExtremeGenAddr=ExtremeGenAddr, L4Port=L4Port, extremeMauType1000BaseLX=extremeMauType1000BaseLX, extremeProduct=extremeProduct, extremeEsrp=extremeEsrp, alpine3804=alpine3804, extremeMauType1000BaseWDMHD=extremeMauType1000BaseWDMHD, extremeMauType1000BaseLX70FD=extremeMauType1000BaseLX70FD, extremeCable=extremeCable, WPACipherSet=WPACipherSet, summit5i=summit5i, extremeV1Traps=extremeV1Traps, summit48=summit48, extremeVC=extremeVC, extremeFdb=extremeFdb, blackDiamond6804=blackDiamond6804, summit1iTX=summit1iTX, summitPx1=summitPx1, summit400_24p=summit400_24p, summit48i=summit48i, summit48si=summit48si, summit24e3=summit24e3, extremeOspf=extremeOspf, extremeSnmpv3=extremeSnmpv3, extremeMauType1000BaseCX=extremeMauType1000BaseCX, summit400_24x=summit400_24x, summit5iTX=summit5iTX, extremeQos=extremeQos, extremeMauType1000BaseLXFD=extremeMauType1000BaseLXFD, extremeEntity=extremeEntity, extremeStp=extremeStp, summit1iSX=summit1iSX, extremeMauType1000BaseZXHD=extremeMauType1000BaseZXHD, alpine3808=alpine3808, extremeMauType1000BaseLX100HD=extremeMauType1000BaseLX100HD, summit4=summit4, PortList=PortList, extremenetworks=extremenetworks, extremeMauType1000BaseZXFD=extremeMauType1000BaseZXFD, extremeMauType1000BaseLX70HD=extremeMauType1000BaseLX70HD, extremeDosMib=extremeDosMib, summit24=summit24, alpine3802=alpine3802, ClientAuthType=ClientAuthType, extremeMauType1000BaseWDMFD=extremeMauType1000BaseWDMFD, extremeMauType1000BaseLX100FD=extremeMauType1000BaseLX100FD, summit1=summit1, summit300_24=summit300_24, summit2=summit2, summit200_48=summit200_48, summit400_48t=summit400_48t, extremeVlan=extremeVlan, summit200_24fx=summit200_24fx, extremeFileTransfer=extremeFileTransfer, WirelessRemoteConnectBindingType=WirelessRemoteConnectBindingType, extremeOids=extremeOids, summit400_24t=summit400_24t, ExtremeDeviceId=ExtremeDeviceId, extremeRtStats=extremeRtStats, summit7iTX=summit7iTX, blackDiamond6816=blackDiamond6816, extremeNPMib=extremeNPMib, blackDiamond6808=blackDiamond6808, blackDiamond6800=blackDiamond6800, WPAKeyMgmtSet=WPAKeyMgmtSet, extremeEnhDosMib=extremeEnhDosMib, summit24e2SX=summit24e2SX, extremeLAC=extremeLAC, extremeSystem=extremeSystem, extremeMauType=extremeMauType, enetSwitch24Port=enetSwitch24Port, extremeTrapPoll=extremeTrapPoll, summit200_24=summit200_24, summit4fx=summit4fx, extremeMisc=extremeMisc, extremeMauType1000BaseCXFD=extremeMauType1000BaseCXFD, extremeEdp=extremeEdp, summit300_48=summit300_48, extremePOSMib=extremePOSMib, extremePort=extremePort, extremeWireless=extremeWireless, extremeQosPolicy=extremeQosPolicy, extremeAP=extremeAP, summit24e2TX=summit24e2TX, summit5iLX=summit5iLX, summit7iSX=summit7iSX, extremeAgent=extremeAgent, extremeMauType1000BaseSXFD=extremeMauType1000BaseSXFD, extremeMauType1000BaseSX=extremeMauType1000BaseSX, extremeStack=extremeStack, summit3=summit3)
