#
# PySNMP MIB module PDN-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-TC
# Produced by pysmi-0.3.4 at Mon Apr 29 20:29:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, iso, Bits, Unsigned32, NotificationType, Counter32, Integer32, Counter64, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity, enterprises, MibIdentifier, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "iso", "Bits", "Unsigned32", "NotificationType", "Counter32", "Integer32", "Counter64", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity", "enterprises", "MibIdentifier", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pdyn = MibIdentifier((1, 3, 6, 1, 4, 1, 1795))
class VnidMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("implicit", 1), ("explicit", 2), ("notagging", 3))

class ClientState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("static", 1), ("dynamic", 2))

class VnidTaggingState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class VnidRange(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(2, 4000)

class SwitchState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class ResetStates(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("noOp", 1), ("reset", 2), ("resetToFactoryDefaults", 3))

class ResultTypes(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("success", 2), ("failure", 3), ("inProgress", 4))

class InitiatorTypes(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("noop", 1), ("telnet", 2), ("console", 3), ("snmp", 4))

class NTPMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("unicast", 1), ("broadcast", 2))

class DNSServerType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("primary", 1), ("secondary", 2))

class MibOidType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("scalar", 1), ("table", 2), ("mib", 3), ("section", 4))

class SocketType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 1), ("stream", 2), ("datagram", 3), ("rawProtocol", 4), ("reliableMessageDelivery", 5), ("sequencedPacket", 6))

class SocketFamily(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23))
    namedValues = NamedValues(("unknown", 1), ("unix", 2), ("darpaInternet", 3), ("darpaIMP", 4), ("pUP", 5), ("cHAOSFamily", 6), ("xeroxNovell", 7), ("nBS", 8), ("eCMA", 9), ("dATAKIT", 10), ("cCITT", 11), ("sNA", 12), ("dECnet", 13), ("directDataLinkInterface", 14), ("dECLAT", 15), ("nSCHyperChannel", 16), ("appleTalk", 17), ("netqorkInterfaceTap", 18), ("iEEE8020ISO8802", 19), ("oSI", 20), ("x25", 21), ("oSIAFI47IDI4", 22), ("uSGovermentOSI", 23))

class SocketState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("closed", 1), ("listen", 2), ("sYNSent", 3), ("sYNRCVD", 4), ("established", 5), ("closeWait", 6), ("fINWait", 7), ("closing", 8), ("lastAck", 9), ("fINWait2", 10), ("timeWait", 11))

class DomainName(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 64)

class SnmpAdminString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class InetAddressType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("primary", 1), ("secondary", 2))

class ManagementType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("inband", 1), ("outband", 2))

class IdslClockMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("triState", 1), ("portCardSinkClock", 2), ("portCardDriveClock", 3), ("portCardDriveClockOnboard", 4))

mibBuilder.exportSymbols("PDN-TC", DomainName=DomainName, DNSServerType=DNSServerType, ClientState=ClientState, VnidRange=VnidRange, VnidTaggingState=VnidTaggingState, SocketType=SocketType, SnmpAdminString=SnmpAdminString, ResultTypes=ResultTypes, IdslClockMode=IdslClockMode, SocketState=SocketState, ResetStates=ResetStates, VnidMode=VnidMode, ManagementType=ManagementType, SwitchState=SwitchState, MibOidType=MibOidType, NTPMode=NTPMode, InitiatorTypes=InitiatorTypes, SocketFamily=SocketFamily, InetAddressType=InetAddressType, pdyn=pdyn)
