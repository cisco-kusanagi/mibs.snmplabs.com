#
# PySNMP MIB module CISCO-VIDEO-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VIDEO-TC
# Produced by pysmi-0.3.4 at Wed May  1 12:02:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Unsigned32, Bits, MibIdentifier, Counter32, IpAddress, NotificationType, Integer32, Counter64, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Unsigned32", "Bits", "MibIdentifier", "Counter32", "IpAddress", "NotificationType", "Integer32", "Counter64", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoVideoTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 763))
ciscoVideoTc.setRevisions(('2010-11-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVideoTc.setRevisionsDescriptions(('Initial version of this MIB module',))
if mibBuilder.loadTexts: ciscoVideoTc.setLastUpdated('201011080000Z')
if mibBuilder.loadTexts: ciscoVideoTc.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVideoTc.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-video@cisco.com')
if mibBuilder.loadTexts: ciscoVideoTc.setDescription('This MIB module defines a collection of common video-related textual conventions to be used in Cisco MIBS for video-capable products and network equipments.')
class CvcVideoResolution(TextualConvention, Integer32):
    reference = 'ITU-T H.261 ITU-R BT.470 : NTSC, PAL, SDTV ITU-R BT.709 : HDTV ISO/IEC 11172 : MPEG-1 IOS/IEC 13818 : MPEG-2 VESA VBE : SVGA IBM VGA/XGA'
    description = "This textual convention contains a list of popoular video resolution definitions. Video resolutions have a variety depending on the standardization organizations and regions, e.g. NTSC, PAL, SDTV, HDTV, MPEG, VESA, etc., which may need to be included for identification. Unnamed formats are shown as width x height. Whenever needed to avoid the leading character being a number in any enum label, 'n' is added as the label prefix. Resolutions not found in the list should use 'unknown'. Format Width Height Label Note SQCIF 128 96 sqcif QCIF 176 144 qcif Quarter CIF QVGA 320 240 qvga Quarter VGA 525-SIF 352 240 sif525 SIF on NTSC CIF 352 288 cif CIF/SIF on PAL 525-HHR 352 480 hhr525 MPEG-2 HHR on NTSC 625-HHR 352 576 hhr625 MPEG-2 HHR on PAL VGA 640 480 vga IBM VGA 525-4SIF 704 480 n4sif525 4SIF on NTSC 525-SD 720 480 sd525 480i/p on NTSC SDTV 4CIF 704 576 n4cif 4CIF/4SIF on PAL 625-SD 720 576 sd625 576i/p on PAL SDTV SVGA 800 600 svga VESA Super VGA XGA 1024 768 xga IBM XGA 720p-HD 1280 720 hd720p 720p on HDTV 4VGA 1280 960 n4vga SXGA 1280 1024 sxga Super XGA 525-16SIF 1408 960 n16sif525 16SIF on NTSC 16CIF 1408 1152 n16cif 16CIF/16SIF on PAL 4SVGA 1600 1200 n4svga 1080p-HD 1920 1088 hd1080p 1080p on HDTV 2Kx1K 2048 1024 n2Kx1K 2Kx1080 2048 1088 n2Kx1080 4XGA 2048 1536 n4xga 16VGA 2560 1920 n16vga 3616x1536 3616 1536 n3616x1536 3672x1536 3680 1536 n3672x1536 4Kx2K 4096 2048 n4Kx2K 4096x2304 4096 2304 n4096x2304 - - - unknown"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29))
    namedValues = NamedValues(("unknown", 0), ("sqcif", 1), ("qcif", 2), ("qvga", 3), ("sif525", 4), ("cif", 5), ("hhr525", 6), ("hhr625", 7), ("vga", 8), ("n4sif525", 9), ("sd525", 10), ("n4cif", 11), ("sd625", 12), ("svga", 13), ("xga", 14), ("hd720p", 15), ("n4vga", 16), ("sxga", 17), ("n16sif525", 18), ("n16cif", 19), ("n4svga", 20), ("hd1080p", 21), ("n2Kx1K", 22), ("n2Kx1080", 23), ("n4xga", 24), ("n16vga", 25), ("n3616x1536", 26), ("n3672x1536", 27), ("n4Kx2K", 28), ("n4096x2304", 29))

class CvcVideoLevel(TextualConvention, Integer32):
    reference = 'ITU-T H.264: Annex A.3 Levels'
    description = 'A value that represents a type of H.263 and H264 level stream. Level 1b (9) Level 1 (10) Level 1.1 (11) Level 1.2 (12) Level 1.3 (13) Level 2 (20) Level 2.1 (21) Level 2.2 (22) Level 3 (30) Level 3.1 (31) Level 3.2 (32) Level 4 (40) Level 4.1 (41) Level 4.2 (42) Level 5 (50) Level 5.1 (51)'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 9, 10, 11, 12, 13, 20, 21, 22, 30, 31, 32, 40, 41, 42, 50, 51))
    namedValues = NamedValues(("unknown", 0), ("level1b", 9), ("level1", 10), ("level1dot1", 11), ("level1dot2", 12), ("level1dot3", 13), ("level2", 20), ("level2dot1", 21), ("level2dot2", 22), ("level3", 30), ("level3dot1", 31), ("level3dot2", 32), ("level4", 40), ("level4dot1", 41), ("level4dot2", 42), ("level5", 50), ("level5dot1", 51))

class CvcVideoProfile(TextualConvention, Integer32):
    reference = 'ITU-T H.263: Annex X.2 Profiles of preferred mode support ITU-T H.264: Annex A.2 Profiles'
    description = 'A value that represents a type of H.263 and H264 profile stream. H.263 Profiles: Profile 0 (10) Profile 1 (11) Profile 2 (12) Profile 3 (13) Profile 4 (14) Profile 5 (15) Profile 6 (16) Profile 7 (17) Profile 8 (18) H.264 Profiles: Baseline Profile (100) Main Profile (101) Extended Profile (102) High Profile (103) High 10 Profile (104) High 4:2:2 Profile (105) High 4:4:4 Predictive Profile (106) High 10 Intra Profile (107) High 4:2:2 Intra Profile (108) High 4:4:4 Intra Profile (109) CAVLC 4:4:4 Intra Profile (110)'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 10, 11, 12, 13, 14, 15, 16, 17, 18, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110))
    namedValues = NamedValues(("unknown", 0), ("h263Profile0", 10), ("h263Profile1", 11), ("h263Profile2", 12), ("h263Profile3", 13), ("h263Profile4", 14), ("h263Profile5", 15), ("h263Profile6", 16), ("h263Profile7", 17), ("h263Profile8", 18), ("h264ProfileBaseline", 100), ("h264ProfileMain", 101), ("h264ProfileExtended", 102), ("h264ProfileHigh", 103), ("h264ProfileHigh10", 104), ("h264ProfileHigh422", 105), ("h264ProfileHigh444Predictive", 106), ("h264ProfileHigh10Intra", 107), ("h264ProfileHigh422Intra", 108), ("h264ProfileHigh444Intra", 109), ("h264ProfileCavlc444Intra", 110))

class CvcVideoCodecAnnexMap(TextualConvention, Bits):
    reference = 'ITU-T H.263 Annex A - Inverse transform accuracy specification Annex B - Hypothetical Reference Decoder Annex C - Considerations for multipoint Annex D - Unrestricted Motion Vector Mode Annex E - Syntax-based Arithmetic Coding mode Annex F - Advanced Prediction mode Annex G - PB-frames mode Annex H - Forward error correction for coded video signal Annex I - Advanced INTRA Coding mode Annex J - Deblocking Filter mode Annex K - Slice Structured mode Annex L - Supplemental enhancement information specification Annex M - Improved PB-frames mode Annex N - Reference Picture selection mode Annex O - Temporal, SNR, and Spatial Scalability mode Annex P - Reference picture resampling Annex Q - Reduced-Resolution Update mode Annex R - Independent Segment Decoding mode Annex S - Alternative INTER VLC mode Annex T - Modified Quantization mode Annex U - Enhanced reference picture selection mode Annex V - Data-partitioned slice mode Annex W - Additional supplemental enhancement information specification ITU-T H.264 Annex C - Hypothetical reference decoder Annex D - Supplemental enhancement information Annex E - Video usability information Annex G - Scalable video coding Annex H - Multiview video coding'
    description = 'A bit value that represents an annex(es) type of video codec. Multiple annexes can be present; bits that are set to 1 indicate the supported annex(es) correspondingly. No annex - 0x000000 (bit 0) Annex D.1 - 0x000001 (bit 1) Annex D.2 - 0x000002 (bit 2) Annex E - 0x000004 (bit 3) Annex F - 0x000008 (bit 4) Annex G - 0x000010 (bit 5) Annex H - 0x000020 (bit 6) Annex I - 0x000040 (bit 7) Annex J - 0x000080 (bit 8) Annex K - 0x000100 (bit 9) Annex L - 0x000200 (bit 10) Annex M - 0x000400 (bit 11) Annex N - 0x000800 (bit 12) Annex O - 0x001000 (bit 13) Annex P - 0x002000 (bit 14) Annex Q - 0x004000 (bit 15) Annex R - 0x008000 (bit 16) Annex S - 0x010000 (bit 17) Annex T - 0x020000 (bit 18) Annex U - 0x040000 (bit 19) Annex V - 0x080000 (bit 20) Annex W - 0x100000 (bit 21)'
    status = 'current'
    namedValues = NamedValues(("annexNone", 0), ("annexD1", 1), ("annexD2", 2), ("annexE", 3), ("annexF", 4), ("annexG", 5), ("annexH", 6), ("annexI", 7), ("annexJ", 8), ("annexK", 9), ("annexL", 10), ("annexM", 11), ("annexN", 12), ("annexO", 13), ("annexP", 14), ("annexQ", 15), ("annexR", 16), ("annexS", 17), ("annexT", 18), ("annexU", 19), ("annexV", 20), ("annexW", 21))

class CvcVideoRtpPayloadFormat(TextualConvention, Integer32):
    reference = 'RFC 2190 - RTP Payload Format for H.263 Video Streams RFC 2429 - RTP Payload Format for the 1998 Version of ITU-T Rec. H.263 Video (H.263+) RFC 4629 - RTP Payload Format for ITU-T Rec. H.263 Video RFC 3984 - RTP Payload Format for H.264 Video'
    description = 'A value that represents a type of the RTP payload format used for video stream. RFC2190 (1) - RTP payload format for video codec H.263 RFC2429 (2) - RTP payload format for video codec H.263 RFC4629 (3) - RTP payload format for video codec H.263 RFC3984 (4) - RTP payload format for video codec H.264'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 0), ("rfc2190", 1), ("rfc2429", 2), ("rfc4629", 3), ("rfc3984", 4))

mibBuilder.exportSymbols("CISCO-VIDEO-TC", CvcVideoResolution=CvcVideoResolution, PYSNMP_MODULE_ID=ciscoVideoTc, CvcVideoLevel=CvcVideoLevel, CvcVideoProfile=CvcVideoProfile, ciscoVideoTc=ciscoVideoTc, CvcVideoCodecAnnexMap=CvcVideoCodecAnnexMap, CvcVideoRtpPayloadFormat=CvcVideoRtpPayloadFormat)
