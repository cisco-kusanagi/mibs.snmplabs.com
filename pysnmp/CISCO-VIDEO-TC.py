#
# PySNMP MIB module CISCO-VIDEO-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VIDEO-TC
# Produced by pysmi-0.3.4 at Mon Apr 29 17:45:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, Gauge32, Bits, MibIdentifier, Integer32, TimeTicks, Counter64, IpAddress, iso, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "Gauge32", "Bits", "MibIdentifier", "Integer32", "TimeTicks", "Counter64", "IpAddress", "iso", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoVideoTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 763))
ciscoVideoTc.setRevisions(('2010-11-08 00:00',))
if mibBuilder.loadTexts: ciscoVideoTc.setLastUpdated('201011080000Z')
if mibBuilder.loadTexts: ciscoVideoTc.setOrganization('Cisco Systems, Inc.')
class CvcVideoResolution(TextualConvention, Integer32):
    reference = 'ITU-T H.261 ITU-R BT.470 : NTSC, PAL, SDTV ITU-R BT.709 : HDTV ISO/IEC 11172 : MPEG-1 IOS/IEC 13818 : MPEG-2 VESA VBE : SVGA IBM VGA/XGA'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29))
    namedValues = NamedValues(("unknown", 0), ("sqcif", 1), ("qcif", 2), ("qvga", 3), ("sif525", 4), ("cif", 5), ("hhr525", 6), ("hhr625", 7), ("vga", 8), ("n4sif525", 9), ("sd525", 10), ("n4cif", 11), ("sd625", 12), ("svga", 13), ("xga", 14), ("hd720p", 15), ("n4vga", 16), ("sxga", 17), ("n16sif525", 18), ("n16cif", 19), ("n4svga", 20), ("hd1080p", 21), ("n2Kx1K", 22), ("n2Kx1080", 23), ("n4xga", 24), ("n16vga", 25), ("n3616x1536", 26), ("n3672x1536", 27), ("n4Kx2K", 28), ("n4096x2304", 29))

class CvcVideoLevel(TextualConvention, Integer32):
    reference = 'ITU-T H.264: Annex A.3 Levels'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 9, 10, 11, 12, 13, 20, 21, 22, 30, 31, 32, 40, 41, 42, 50, 51))
    namedValues = NamedValues(("unknown", 0), ("level1b", 9), ("level1", 10), ("level1dot1", 11), ("level1dot2", 12), ("level1dot3", 13), ("level2", 20), ("level2dot1", 21), ("level2dot2", 22), ("level3", 30), ("level3dot1", 31), ("level3dot2", 32), ("level4", 40), ("level4dot1", 41), ("level4dot2", 42), ("level5", 50), ("level5dot1", 51))

class CvcVideoProfile(TextualConvention, Integer32):
    reference = 'ITU-T H.263: Annex X.2 Profiles of preferred mode support ITU-T H.264: Annex A.2 Profiles'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 10, 11, 12, 13, 14, 15, 16, 17, 18, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110))
    namedValues = NamedValues(("unknown", 0), ("h263Profile0", 10), ("h263Profile1", 11), ("h263Profile2", 12), ("h263Profile3", 13), ("h263Profile4", 14), ("h263Profile5", 15), ("h263Profile6", 16), ("h263Profile7", 17), ("h263Profile8", 18), ("h264ProfileBaseline", 100), ("h264ProfileMain", 101), ("h264ProfileExtended", 102), ("h264ProfileHigh", 103), ("h264ProfileHigh10", 104), ("h264ProfileHigh422", 105), ("h264ProfileHigh444Predictive", 106), ("h264ProfileHigh10Intra", 107), ("h264ProfileHigh422Intra", 108), ("h264ProfileHigh444Intra", 109), ("h264ProfileCavlc444Intra", 110))

class CvcVideoCodecAnnexMap(TextualConvention, Bits):
    reference = 'ITU-T H.263 Annex A - Inverse transform accuracy specification Annex B - Hypothetical Reference Decoder Annex C - Considerations for multipoint Annex D - Unrestricted Motion Vector Mode Annex E - Syntax-based Arithmetic Coding mode Annex F - Advanced Prediction mode Annex G - PB-frames mode Annex H - Forward error correction for coded video signal Annex I - Advanced INTRA Coding mode Annex J - Deblocking Filter mode Annex K - Slice Structured mode Annex L - Supplemental enhancement information specification Annex M - Improved PB-frames mode Annex N - Reference Picture selection mode Annex O - Temporal, SNR, and Spatial Scalability mode Annex P - Reference picture resampling Annex Q - Reduced-Resolution Update mode Annex R - Independent Segment Decoding mode Annex S - Alternative INTER VLC mode Annex T - Modified Quantization mode Annex U - Enhanced reference picture selection mode Annex V - Data-partitioned slice mode Annex W - Additional supplemental enhancement information specification ITU-T H.264 Annex C - Hypothetical reference decoder Annex D - Supplemental enhancement information Annex E - Video usability information Annex G - Scalable video coding Annex H - Multiview video coding'
    status = 'current'
    namedValues = NamedValues(("annexNone", 0), ("annexD1", 1), ("annexD2", 2), ("annexE", 3), ("annexF", 4), ("annexG", 5), ("annexH", 6), ("annexI", 7), ("annexJ", 8), ("annexK", 9), ("annexL", 10), ("annexM", 11), ("annexN", 12), ("annexO", 13), ("annexP", 14), ("annexQ", 15), ("annexR", 16), ("annexS", 17), ("annexT", 18), ("annexU", 19), ("annexV", 20), ("annexW", 21))

class CvcVideoRtpPayloadFormat(TextualConvention, Integer32):
    reference = 'RFC 2190 - RTP Payload Format for H.263 Video Streams RFC 2429 - RTP Payload Format for the 1998 Version of ITU-T Rec. H.263 Video (H.263+) RFC 4629 - RTP Payload Format for ITU-T Rec. H.263 Video RFC 3984 - RTP Payload Format for H.264 Video'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 0), ("rfc2190", 1), ("rfc2429", 2), ("rfc4629", 3), ("rfc3984", 4))

mibBuilder.exportSymbols("CISCO-VIDEO-TC", CvcVideoLevel=CvcVideoLevel, PYSNMP_MODULE_ID=ciscoVideoTc, ciscoVideoTc=ciscoVideoTc, CvcVideoRtpPayloadFormat=CvcVideoRtpPayloadFormat, CvcVideoCodecAnnexMap=CvcVideoCodecAnnexMap, CvcVideoProfile=CvcVideoProfile, CvcVideoResolution=CvcVideoResolution)
