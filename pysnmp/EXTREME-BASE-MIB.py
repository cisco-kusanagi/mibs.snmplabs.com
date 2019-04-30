#
# PySNMP MIB module EXTREME-BASE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EXTREME-BASE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:53:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Unsigned32, iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, ObjectIdentity, Bits, ModuleIdentity, MibIdentifier, Counter64, Counter32, NotificationType, Integer32, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "ObjectIdentity", "Bits", "ModuleIdentity", "MibIdentifier", "Counter64", "Counter32", "NotificationType", "Integer32", "IpAddress", "TimeTicks")
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
    status = 'current'

class L4Port(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 65535), )
class ExtremeGenAddr(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 20)

class ExtremeDeviceId(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class WPACipherSet(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("none", 0), ("wep64", 1), ("tkip", 2), ("wrap", 3), ("ccmp", 4), ("wep128", 5), ("other", 6))

class WPAKeyMgmtSet(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("none", 0), ("dot1x", 1), ("psk", 2))

class ClientAuthType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("none", 0), ("open", 1), ("wep", 2), ("mac-based", 3), ("dot1x", 4), ("wpa-psk", 5), ("web-based", 6), ("wpa", 7), ("wpa2", 8), ("wpa2-psk", 9))

class WirelessRemoteConnectBindingType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("mac-address", 1), ("serial-number", 2), ("ip-address", 3))

mibBuilder.exportSymbols("EXTREME-BASE-MIB", summit2=summit2, summit48i=summit48i, summit5iTX=summit5iTX, extremeVlan=extremeVlan, extremeFdb=extremeFdb, summit24=summit24, summit1=summit1, extremeEnhDosMib=extremeEnhDosMib, summit5i=summit5i, extremeWireless=extremeWireless, summit48=summit48, L4Port=L4Port, extremeMauType1000BaseLX100HD=extremeMauType1000BaseLX100HD, extremeNetFlow=extremeNetFlow, summit200_24=summit200_24, extremeMauType1000BaseSX=extremeMauType1000BaseSX, extremeMauType1000BaseWDMFD=extremeMauType1000BaseWDMFD, extremeMauType1000BaseSXFD=extremeMauType1000BaseSXFD, summit24e2SX=summit24e2SX, extremePort=extremePort, summit1iTX=summit1iTX, summit200_48=summit200_48, extremeSlb=extremeSlb, extremeAP=extremeAP, summit300_24=summit300_24, extremeMisc=extremeMisc, summit4fx=summit4fx, extremeQos=extremeQos, summit48si=summit48si, alpine3804=alpine3804, extremeMauType1000BaseLX70FD=extremeMauType1000BaseLX70FD, summit400_24t=summit400_24t, extremeCable=extremeCable, summit200_24fx=summit200_24fx, extremeRtStats=extremeRtStats, extremeLAC=extremeLAC, extremeStack=extremeStack, summit1iSX=summit1iSX, extremeMauType1000BaseLX=extremeMauType1000BaseLX, blackDiamond6816=blackDiamond6816, blackDiamond6800=blackDiamond6800, extremeEdp=extremeEdp, ExtremeDeviceId=ExtremeDeviceId, extremeMauType1000BaseLX70HD=extremeMauType1000BaseLX70HD, summit7iSX=summit7iSX, PortList=PortList, extremeMauType1000BaseWDMHD=extremeMauType1000BaseWDMHD, extremeNPMib=extremeNPMib, summit3=summit3, extremeMauType=extremeMauType, extremeSystem=extremeSystem, alpine3808=alpine3808, extremeTrapPoll=extremeTrapPoll, extremeMauType1000BaseCXFD=extremeMauType1000BaseCXFD, extremeFileTransfer=extremeFileTransfer, summit400_24x=summit400_24x, blackDiamond6804=blackDiamond6804, summit7iTX=summit7iTX, extremeMauType1000BaseZXFD=extremeMauType1000BaseZXFD, summit5iLX=summit5iLX, extremeOids=extremeOids, alpine3802=alpine3802, extremeMauType1000BaseCX=extremeMauType1000BaseCX, extremeDlcs=extremeDlcs, summit24e3=summit24e3, extremeV2Traps=extremeV2Traps, extremeOspf=extremeOspf, extremeQosPolicy=extremeQosPolicy, summit400_24p=summit400_24p, extremenetworks=extremenetworks, summit300_48=summit300_48, extremeStp=extremeStp, ClientAuthType=ClientAuthType, extremeV1Traps=extremeV1Traps, extremeEsrp=extremeEsrp, blackDiamond6808=blackDiamond6808, WirelessRemoteConnectBindingType=WirelessRemoteConnectBindingType, extremeMauType1000BaseLX100FD=extremeMauType1000BaseLX100FD, extremeEntity=extremeEntity, WPACipherSet=WPACipherSet, enetSwitch24Port=enetSwitch24Port, summit400_48t=summit400_48t, extremeSnmpv3=extremeSnmpv3, summitPx1=summitPx1, extremeMauType1000BaseLXFD=extremeMauType1000BaseLXFD, summit24e2TX=summit24e2TX, extremeProduct=extremeProduct, summit4=summit4, extremePOSMib=extremePOSMib, WPAKeyMgmtSet=WPAKeyMgmtSet, extremeAgent=extremeAgent, extremeMauType1000BaseZXHD=extremeMauType1000BaseZXHD, ExtremeGenAddr=ExtremeGenAddr, extremeVC=extremeVC, extremeDosMib=extremeDosMib)
