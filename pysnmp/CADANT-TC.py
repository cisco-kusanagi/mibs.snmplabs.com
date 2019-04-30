#
# PySNMP MIB module CADANT-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CADANT-TC
# Produced by pysmi-0.3.4 at Mon Apr 29 17:26:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
cadant, = mibBuilder.importSymbols("CADANT-PRODUCTS-MIB", "cadant")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, IpAddress, Gauge32, Integer32, NotificationType, ModuleIdentity, iso, ObjectIdentity, Counter64, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "IpAddress", "Gauge32", "Integer32", "NotificationType", "ModuleIdentity", "iso", "ObjectIdentity", "Counter64", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Bits", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cadTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 4998, 0))
cadTextualConventions.setRevisions(('2015-07-16 00:00', '2015-06-24 00:00', '2015-06-01 00:00', '2014-12-03 00:00', '2014-12-01 00:00', '2014-10-14 00:00', '2014-08-01 00:00', '2014-03-13 00:00', '2014-01-13 00:00', '2013-10-23 00:00', '2013-05-16 00:00', '2012-04-11 00:00', '2012-02-23 00:00', '2011-12-08 00:00', '2011-06-09 00:00', '2010-11-22 00:00', '2011-02-24 00:00', '2010-12-14 00:00', '2010-10-28 00:00', '2010-05-18 00:00', '2010-02-23 00:00', '2010-01-11 00:00', '2009-10-15 00:00', '2009-09-14 00:00', '2009-08-28 00:00', '2009-08-19 00:00', '2009-07-10 00:00', '2008-10-23 00:00', '2008-08-06 00:00', '2007-11-05 00:00', '2007-06-25 00:00', '2006-10-16 00:00', '2006-08-23 00:00', '2006-07-27 00:00', '2006-07-27 00:00', '2005-12-02 00:00', '2005-08-30 00:00', '2005-09-23 00:00', '2005-08-31 00:00', '2004-11-12 00:00', '2004-09-15 00:00', '2004-03-09 00:00', '2003-12-18 00:00', '2003-08-20 00:00', '2003-06-08 00:00', '2003-05-08 00:00', '2003-04-21 00:00', '2003-04-04 00:00', '2003-04-01 00:00', '2003-03-31 00:00', '2003-03-17 00:00', '2002-11-01 00:00', '2002-10-25 00:00', '2002-10-16 00:00', '2002-09-25 00:00', '2001-02-03 00:00',))
if mibBuilder.loadTexts: cadTextualConventions.setLastUpdated('201507160000Z')
if mibBuilder.loadTexts: cadTextualConventions.setOrganization('Arris International Inc')
class CardId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 99)

class PortId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 392)

class CardType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 98))
    namedValues = NamedValues(("invalid", 0), ("dcam", 1), ("ucam", 2), ("rsm", 3), ("fan", 4), ("pem", 5), ("ccm", 6), ("cdm", 7), ("sam", 8), ("unknown", 98))

class CardSubType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 98))
    namedValues = NamedValues(("invalid", 0), ("dcam192d", 1), ("ucam96u", 2), ("rsm56g", 3), ("dcam144d", 4), ("fanA", 7), ("fanB", 8), ("fanC", 9), ("pemA", 10), ("pemB", 11), ("ccmA", 12), ("ccmB", 13), ("cdmA", 14), ("cdmB", 15), ("sam", 16), ("unknown", 98))

class CerCardType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 98))
    namedValues = NamedValues(("invalid", 0), ("fan", 1), ("pem", 2), ("ccm", 3), ("cdm", 4), ("sam", 5), ("rsm", 6), ("ucam", 7), ("dcam", 8), ("unknown", 98))

class CerCardSubType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 98))
    namedValues = NamedValues(("invalid", 0), ("fan", 1), ("pem", 2), ("ccm", 3), ("cdm", 4), ("sam", 5), ("rsm10g", 6), ("ucam96m24c", 7), ("dcam192m8cAnnexA", 8), ("dcam256m8cAnnexB", 9), ("unknown", 98))

class PortType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 98))
    namedValues = NamedValues(("invalid", 0), ("ureceiver", 1), ("uchannel", 2), ("eport10BaseT", 3), ("eport100BaseT", 4), ("eport1000BaseT", 5), ("eport10000BaseT", 6), ("macport", 8), ("dchannelDocsis", 9), ("dchannelVideo", 10), ("linkAgg", 11), ("dchannelVideoReplica", 12), ("dchannelOfdm", 13), ("unknown", 98))

class CerPortType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 98))
    namedValues = NamedValues(("invalid", 0), ("ureceiver", 1), ("uchannel", 2), ("eport10BaseT", 3), ("eport100BaseT", 4), ("eport1000BaseT", 5), ("eport10000BaseT", 6), ("macport", 8), ("dchannelDocsis", 9), ("dchannelVideo", 10), ("linkAgg", 11), ("dchannelVideoreplica", 12), ("dchannelOfdm", 13), ("unknown", 98))

class PortMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("invalid", 0), ("autoNegotiate", 1), ("fullDuplex100Mpbs", 2), ("halfDuplex100Mpbs", 3), ("fullDuplex10Mpbs", 4), ("halfDuplex10Mpbs", 5), ("fullDuplex1000Mpbs", 6), ("halfDuplex1000Mpbs", 7), ("fullDuplex10000Mpbs", 8))

class PortDetectedMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34))
    namedValues = NamedValues(("invalid", 0), ("fullDuplex100Mpbs", 2), ("halfDuplex100Mpbs", 3), ("fullDuplex10Mpbs", 4), ("halfDuplex10Mpbs", 5), ("fullDuplex1000Mpbs", 6), ("halfDuplex1000Mpbs", 7), ("fullDuplex10000Mpbs", 8), ("sfpFullDuplex1000BaseT", 9), ("sfpHalfDuplex1000BaseT", 10), ("sfpFullDuplex100BaseT", 11), ("sfpHalfDuplex100BaseT", 12), ("sfpFullDuplex10BaseT", 13), ("sfpHalfDuplex10BaseT", 14), ("sfpFullDuplex1000BaseSX", 15), ("sfpFullDuplex1000BaseLX", 16), ("sfpFullDuplex1000BaseLH", 17), ("sfpFullDuplex1000BaseLXLH", 18), ("sfpFullDuplex1000BaseZX", 19), ("sfpFullDuplex1000BaseCWDM", 20), ("sfpFullDuplex1000BaseDWDM", 21), ("xfpFullDuplex10GBaseSR", 22), ("xfpFullDuplex10GBaseLRM", 23), ("xfpFullDuplex10GBaseLR", 24), ("xfpFullDuplex10GBaseER", 25), ("xfpFullDuplex10GBaseZR", 26), ("xfpFullDuplex10GBaseLX4", 27), ("xfpFullDuplex10GBaseDWDM", 28), ("sfpFullDuplex10GBaseSR", 29), ("sfpFullDuplex10GBaseLRM", 30), ("sfpFullDuplex10GBaseLR", 31), ("sfpFullDuplex10GBaseER", 32), ("sfpFullDuplex10GBaseZR", 33), ("unknown", 34))

class FlowControlMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("invalid", 0), ("on", 1), ("off", 2), ("desired", 3), ("unknown", 4))

class AdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class PrimaryState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("is", 1), ("oos", 2))

class SecondaryState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("notapplicable", 0), ("manual", 1), ("fault", 2), ("diagnostic", 3), ("overload", 4), ("normal", 5), ("degrade", 6), ("initializing", 7), ("swdownload", 8), ("firmwarepump", 9), ("powerup", 10), ("bootdkm", 11))

class UnknownState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("known", 0), ("unknown", 1))

class DuplexStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("notapplicable", 0), ("active", 1), ("standby", 2), ("simplex", 3), ("protected", 4))

class MacPortId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 416)

class MacPortIdWithInvalid(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 416)

class EqActionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("notapplicable", 0), ("initialize", 1), ("switch", 2), ("remove", 3), ("restorecond", 4), ("restoreuncd", 5), ("systemreset", 6), ("cardreset", 7))

class OverloadStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("normal", 1), ("yellow", 2), ("red", 3))

class OverloadThreshold(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("low", 0), ("medlow", 1), ("med", 2), ("medhigh", 3), ("high", 4))

class DiskVolumeUsageLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("normal", 1), ("minor", 2), ("major", 3), ("critical", 4))

class CadBridgeGroupId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(33, 255)

class CadBridgePortType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("cm", 1), ("cpeauth", 2), ("cpeunauth", 3), ("any", 4), ("none", 5))

class VlanId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 1000000)

class FlowActivityState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("needy", 1), ("normal", 2), ("greedy", 3))

class InetAddressIPv4or6(TextualConvention, OctetString):
    reference = 'InetAddress from INET-ADDRESS-MIB, RFC2851'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(4, 4), ValueSizeConstraint(8, 8), ValueSizeConstraint(16, 16), ValueSizeConstraint(20, 20), )
class LineType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("console", 1), ("vty", 2))

class AAAmethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 5))
    namedValues = NamedValues(("none", 1), ("line", 2), ("local", 4), ("group", 5))

class SshService(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("terminal", 1), ("sftp", 2))

class SshAuthMethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("password", 1), ("public-key", 2))

class SshCipher(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("other", 0), ("threedes", 1), ("arcfour", 2), ("blowfish", 3), ("cast", 4), ("aes", 5))

class SshCipherType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("other", 1), ("threedes", 2), ("arcfour", 3), ("blowfish", 4), ("cast128", 5), ("aes128", 6), ("aes192", 7), ("aes256", 8), ("des", 9), ("rc4", 10))

class SshMacAlg(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("none", 1), ("hmac-sha1", 2), ("hmac-sha1-96", 3), ("hmac-md5", 4), ("hmac-md5-96", 5))

class SshProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ssh1", 1), ("ssh2", 2), ("ssh1ssh2", 3))

class SshKeyType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("dsa1024", 1), ("rsa2048", 2))

class SshKeyExchangeMethod(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("dh-gr1-sha1", 0), ("dh-gr14-sha1", 1))

class CadDouble(TextualConvention, Counter64):
    status = 'current'
    displayHint = 'd-10'

class FirmwareSource(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("committed", 1), ("transient", 2), ("boot1", 3), ("boot2", 4), ("unknown", 5))

class PicType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 98))
    namedValues = NamedValues(("invalid", 0), ("dcamLeft", 1), ("dcamRight", 2), ("dcam", 3), ("ucamRight", 4), ("ucam", 5), ("rsm", 6), ("unknown", 98))

class CerPicType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 98))
    namedValues = NamedValues(("invalid", 0), ("dcamLowPic8c", 1), ("dcamHighPic8c", 2), ("dcamSparePic8c", 3), ("ucamHighPic24c", 4), ("ucamSparePic24c", 5), ("rsmPic", 6), ("unknown", 98))

class CadExtAclCondition(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("na", 0), ("eq", 1), ("ne", 2), ("lt", 3), ("le", 4), ("gt", 5), ("ge", 6), ("range", 7))

class ServerType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("telnet", 1), ("ftp", 2), ("snmp", 3), ("syslog", 4), ("radius", 5), ("tacacs", 6), ("other", 7))

class AccountingType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("start-stop", 1), ("stop-only", 2))

class CadIfDirection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("in", 1), ("out", 2))

class CadIpPort(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 65535), ValueRangeConstraint(-1, -1), )
class CadIpTos(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class CadIpTosMask(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(30, 30), ValueRangeConstraint(224, 224), ValueRangeConstraint(254, 254), ValueRangeConstraint(255, 255), )
class CadProtocolType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 255), ValueRangeConstraint(-1, -1), )
class CadTcpFlags(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("urg", 0), ("ack", 1), ("push", 2), ("rst", 3), ("syn", 4), ("fin", 5))

class CadAclType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("none", 0), ("std-access-list", 1), ("ext-access-list", 2), ("rate-limit-access-list", 3), ("remark", 4), ("ipv6-access-list", 5))

class CadAclString(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class OUIAddress(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

class CadCpeDeviceTypes(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("cable-modem", 0), ("cpe", 1), ("ps", 2), ("mta", 3), ("stb", 4), ("tea", 5), ("erouter", 6), ("dva", 7), ("sg", 8), ("reserved9", 9), ("reserved10", 10), ("reserved11", 11), ("reserved12", 12), ("reserved13", 13), ("reserved14", 14), ("reserved15", 15), ("reserved16", 16), ("reserved17", 17), ("reserved18", 18), ("reserved19", 19), ("reserved20", 20), ("reserved21", 21), ("reserved22", 22), ("reserved23", 23), ("reserved24", 24), ("reserved25", 25), ("reserved26", 26), ("reserved27", 27), ("reserved28", 28), ("reserved29", 29), ("reserved30", 30), ("reserved31", 31))

class AdminSrcAddrType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))
    namedValues = NamedValues(("other", 1), ("ftp", 2), ("http", 3), ("ipdr", 4), ("legal-intercept", 5), ("ntp", 6), ("pc-dqos", 7), ("pc-mm", 8), ("remote-query", 9), ("snmp-trap", 10), ("ssh", 11), ("syslog", 12), ("radius", 13), ("tacacs", 14), ("telnet", 15), ("dns", 16))

mibBuilder.exportSymbols("CADANT-TC", CadDouble=CadDouble, PrimaryState=PrimaryState, UnknownState=UnknownState, PortType=PortType, PortDetectedMode=PortDetectedMode, DiskVolumeUsageLevel=DiskVolumeUsageLevel, LineType=LineType, FirmwareSource=FirmwareSource, CadBridgeGroupId=CadBridgeGroupId, CerPicType=CerPicType, FlowControlMode=FlowControlMode, CardType=CardType, OUIAddress=OUIAddress, MacPortId=MacPortId, VlanId=VlanId, CardId=CardId, OverloadThreshold=OverloadThreshold, CadCpeDeviceTypes=CadCpeDeviceTypes, PYSNMP_MODULE_ID=cadTextualConventions, SshCipherType=SshCipherType, cadTextualConventions=cadTextualConventions, AdminState=AdminState, ServerType=ServerType, InetAddressIPv4or6=InetAddressIPv4or6, CadAclType=CadAclType, CadIpTosMask=CadIpTosMask, CadIpPort=CadIpPort, OverloadStatus=OverloadStatus, SecondaryState=SecondaryState, SshProtocol=SshProtocol, PicType=PicType, AAAmethod=AAAmethod, CerCardType=CerCardType, CerCardSubType=CerCardSubType, CadProtocolType=CadProtocolType, CardSubType=CardSubType, DuplexStatus=DuplexStatus, CadExtAclCondition=CadExtAclCondition, CadIpTos=CadIpTos, SshCipher=SshCipher, CadTcpFlags=CadTcpFlags, CadIfDirection=CadIfDirection, SshService=SshService, FlowActivityState=FlowActivityState, AdminSrcAddrType=AdminSrcAddrType, SshAuthMethod=SshAuthMethod, PortMode=PortMode, SshKeyType=SshKeyType, PortId=PortId, CerPortType=CerPortType, MacPortIdWithInvalid=MacPortIdWithInvalid, CadBridgePortType=CadBridgePortType, CadAclString=CadAclString, SshMacAlg=SshMacAlg, SshKeyExchangeMethod=SshKeyExchangeMethod, EqActionType=EqActionType, AccountingType=AccountingType)
