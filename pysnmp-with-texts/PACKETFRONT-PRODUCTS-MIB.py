#
# PySNMP MIB module PACKETFRONT-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PACKETFRONT-PRODUCTS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:36:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
pfProduct, pfModules = mibBuilder.importSymbols("PACKETFRONT-SMI", "pfProduct", "pfModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, NotificationType, ObjectIdentity, Bits, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier, Gauge32, ModuleIdentity, iso, Integer32, Unsigned32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "ObjectIdentity", "Bits", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier", "Gauge32", "ModuleIdentity", "iso", "Integer32", "Unsigned32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pfProductsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9303, 5, 2))
pfProductsMIB.setRevisions(('2010-05-17 14:10', '2009-04-14 12:29', '2009-03-23 10:53', '2007-05-14 12:38', '2006-01-25 13:30', '2004-10-20 14:34', '2003-11-04 00:01',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: pfProductsMIB.setRevisionsDescriptions(('Added mediastar (MS) product group, updated DRG group', 'Added service engine (SE) product group', 'Updated telephone information in contact-info', 'Generation from PACKETFRONT-MIB', 'Updated to reflect PacketFronts new corporate address', 'Added the ASR10K platorm', 'Added the IPD1116C platform',))
if mibBuilder.loadTexts: pfProductsMIB.setLastUpdated('201005171410Z')
if mibBuilder.loadTexts: pfProductsMIB.setOrganization('PacketFront Systems AB')
if mibBuilder.loadTexts: pfProductsMIB.setContactInfo('PacketFront Systems AB Customer Service Mail : Isafjordsgatan 35 SE-164 28 Kista Sweden Tel : +46 8 5090 1500 E-mail: snmp@packetfront.com Web : http://www.packetfront.com')
if mibBuilder.loadTexts: pfProductsMIB.setDescription('The PacketFront management information base describing product families and the products within those families')
asr = ObjectIdentity((1, 3, 6, 1, 4, 1, 9303, 1, 1))
if mibBuilder.loadTexts: asr.setStatus('current')
if mibBuilder.loadTexts: asr.setDescription('The Access Switching Router (ASR) product group')
ipd = ObjectIdentity((1, 3, 6, 1, 4, 1, 9303, 1, 2))
if mibBuilder.loadTexts: ipd.setStatus('current')
if mibBuilder.loadTexts: ipd.setDescription('The IP DSLAM (IPD) product group')
drg = ObjectIdentity((1, 3, 6, 1, 4, 1, 9303, 1, 3))
if mibBuilder.loadTexts: drg.setStatus('current')
if mibBuilder.loadTexts: drg.setDescription('The Digital Residential Gateway (DRG) product group')
se = ObjectIdentity((1, 3, 6, 1, 4, 1, 9303, 1, 4))
if mibBuilder.loadTexts: se.setStatus('current')
if mibBuilder.loadTexts: se.setDescription('The Service Engine (SE) product group')
ms = ObjectIdentity((1, 3, 6, 1, 4, 1, 9303, 1, 5))
if mibBuilder.loadTexts: ms.setStatus('current')
if mibBuilder.loadTexts: ms.setDescription('The MetroStar (MS) product group')
asr4108C = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 1))
asr4116C = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 2))
asr4124C = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 3))
asr4208FM = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 4))
asr4216FM = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 5))
asr4224FM = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 6))
asr4308FV = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 7))
asr4316FV = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 8))
asr4324FV = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 9))
asr4408SFV = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 10))
asr4416SFV = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 11))
asr4424SFV = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 12))
asr4508SFM = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 13))
asr4516SFM = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 14))
asr4524SFM = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 15))
asr4608SFS = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 16))
asr4616SFS = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 17))
asr4624SFS = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 18))
asr3108VDSL = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 19))
asr3116VDSL = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 20))
asr3124VDSL = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 21))
asr3208VDSL = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 22))
asr3216VDSL = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 23))
asr3224VDSL = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 24))
asr3308VDSL = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 25))
asr3316VDSL = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 26))
asr3324VDSL = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 27))
asr4708SFL = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 28))
asr4716SFL = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 29))
asr4724SFL = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 30))
asr4108Cco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 31))
asr4116Cco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 32))
asr4124Cco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 33))
asr4208FMco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 34))
asr4216FMco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 35))
asr4224FMco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 36))
asr4308FVco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 37))
asr4316FVco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 38))
asr4324FVco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 39))
asr4508SFMco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 40))
asr4516SFMco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 41))
asr4524SFMco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 42))
asr4608SFSco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 43))
asr4616SFSco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 44))
asr4624SFSco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 45))
asr4708SFLco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 46))
asr4716SFLco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 47))
asr4724SFLco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 48))
asr10132co = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 49))
asr5124Cacco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 50))
asr5124Cdcco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 51))
asr5224FMacco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 52))
asr5224FMdcco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 53))
asr5624FSacco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 54))
asr5624FSdcco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 55))
asr5724FLacco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 56))
asr5724FLdcco = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 1, 57))
ipd1116C = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 2, 1))
drg100 = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 3, 1))
drg340 = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 3, 2))
drg560 = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 3, 3))
drg580 = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 3, 4))
evm01 = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 3, 5))
drg600Access = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 3, 6))
drg600Telephony = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 3, 7))
drg600Wifi = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 3, 8))
drg615 = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 3, 7))
drg635 = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 3, 8))
drg701 = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 3, 9))
drg702 = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 3, 10))
drg703 = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 3, 11))
drg711 = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 3, 12))
drg712 = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 3, 13))
drg714 = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 3, 14))
drg716 = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 3, 15))
drg718 = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 3, 16))
drg719 = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 3, 17))
ms2016ac = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 5, 1))
ms2016dc = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 5, 2))
ms3028ac = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 5, 3))
ms3028dc = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 5, 4))
ms3128ac = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 5, 5))
ms3128dc = MibIdentifier((1, 3, 6, 1, 4, 1, 9303, 1, 5, 6))
mibBuilder.exportSymbols("PACKETFRONT-PRODUCTS-MIB", asr4508SFM=asr4508SFM, drg635=drg635, asr4108Cco=asr4108Cco, asr5624FSacco=asr5624FSacco, asr5124Cdcco=asr5124Cdcco, asr4616SFSco=asr4616SFSco, asr4524SFM=asr4524SFM, drg340=drg340, asr10132co=asr10132co, drg714=drg714, drg580=drg580, ms=ms, drg701=drg701, drg712=drg712, asr4124C=asr4124C, asr4716SFL=asr4716SFL, drg600Telephony=drg600Telephony, asr4116Cco=asr4116Cco, asr3316VDSL=asr3316VDSL, ms3128dc=ms3128dc, ipd1116C=ipd1116C, PYSNMP_MODULE_ID=pfProductsMIB, asr5124Cacco=asr5124Cacco, asr4508SFMco=asr4508SFMco, drg718=drg718, asr5224FMdcco=asr5224FMdcco, drg600Access=drg600Access, asr3116VDSL=asr3116VDSL, asr4116C=asr4116C, asr3224VDSL=asr3224VDSL, asr3324VDSL=asr3324VDSL, asr4308FV=asr4308FV, asr4216FMco=asr4216FMco, asr3108VDSL=asr3108VDSL, asr4608SFS=asr4608SFS, evm01=evm01, asr4408SFV=asr4408SFV, asr4708SFL=asr4708SFL, ms2016dc=ms2016dc, asr4324FV=asr4324FV, asr3208VDSL=asr3208VDSL, asr4224FMco=asr4224FMco, asr4424SFV=asr4424SFV, asr4208FM=asr4208FM, asr4716SFLco=asr4716SFLco, asr3216VDSL=asr3216VDSL, asr5724FLacco=asr5724FLacco, drg702=drg702, asr4724SFL=asr4724SFL, asr4216FM=asr4216FM, asr5224FMacco=asr5224FMacco, asr4416SFV=asr4416SFV, drg711=drg711, se=se, asr3308VDSL=asr3308VDSL, asr4608SFSco=asr4608SFSco, drg719=drg719, asr4324FVco=asr4324FVco, asr5724FLdcco=asr5724FLdcco, asr4308FVco=asr4308FVco, drg615=drg615, asr4616SFS=asr4616SFS, asr4624SFSco=asr4624SFSco, ipd=ipd, asr3124VDSL=asr3124VDSL, asr4516SFM=asr4516SFM, asr4516SFMco=asr4516SFMco, ms3028dc=ms3028dc, asr4708SFLco=asr4708SFLco, asr4724SFLco=asr4724SFLco, asr4524SFMco=asr4524SFMco, asr4316FVco=asr4316FVco, asr4624SFS=asr4624SFS, asr4316FV=asr4316FV, asr5624FSdcco=asr5624FSdcco, drg703=drg703, drg=drg, ms3128ac=ms3128ac, asr4108C=asr4108C, asr4124Cco=asr4124Cco, asr=asr, asr4208FMco=asr4208FMco, drg560=drg560, drg100=drg100, ms3028ac=ms3028ac, pfProductsMIB=pfProductsMIB, drg716=drg716, ms2016ac=ms2016ac, drg600Wifi=drg600Wifi, asr4224FM=asr4224FM)
