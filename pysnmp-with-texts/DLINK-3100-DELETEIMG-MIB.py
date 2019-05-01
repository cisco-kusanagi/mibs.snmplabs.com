#
# PySNMP MIB module DLINK-3100-DELETEIMG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DLINK-3100-DELETEIMG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:48:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
rnd, = mibBuilder.importSymbols("DLINK-3100-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits, NotificationType, Counter32, TimeTicks, ModuleIdentity, Counter64, ObjectIdentity, Unsigned32, MibIdentifier, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits", "NotificationType", "Counter32", "TimeTicks", "ModuleIdentity", "Counter64", "ObjectIdentity", "Unsigned32", "MibIdentifier", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DELETEIMGName(TextualConvention, Integer32):
    description = 'Specifies name of image to be deleted: 1- image_1. 2- image_2.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("image1", 1), ("image2", 2))

rlDeleteImg = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 142))
rlDeleteImg.setRevisions(('2007-11-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlDeleteImg.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rlDeleteImg.setLastUpdated('2007111800Z')
if mibBuilder.loadTexts: rlDeleteImg.setOrganization('Dlink, Inc.')
if mibBuilder.loadTexts: rlDeleteImg.setContactInfo('www.dlink.com')
if mibBuilder.loadTexts: rlDeleteImg.setDescription(' Dlink delete image MIB')
rlDeleteImgTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 142, 1), )
if mibBuilder.loadTexts: rlDeleteImgTable.setStatus('current')
if mibBuilder.loadTexts: rlDeleteImgTable.setDescription(" Dlink's table for delete image ")
rlDeleteImgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 142, 1, 1), ).setIndexNames((0, "DLINK-3100-DELETEIMG-MIB", "rlDeleteImgKey"))
if mibBuilder.loadTexts: rlDeleteImgEntry.setStatus('current')
if mibBuilder.loadTexts: rlDeleteImgEntry.setDescription(' Entry in rlDeleteImgTable.')
rlDeleteImgKey = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 142, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1)))
if mibBuilder.loadTexts: rlDeleteImgKey.setStatus('current')
if mibBuilder.loadTexts: rlDeleteImgKey.setDescription("Variable that specifies the key of the MIB's single entry")
rlDeleteImgUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 142, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDeleteImgUnit.setStatus('current')
if mibBuilder.loadTexts: rlDeleteImgUnit.setDescription(" Unit number for Dlink's delete image action MIB")
rlDeleteImgName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 142, 1, 1, 3), DELETEIMGName()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDeleteImgName.setStatus('current')
if mibBuilder.loadTexts: rlDeleteImgName.setDescription(" Image name for Dlink's delete image action MIB")
mibBuilder.exportSymbols("DLINK-3100-DELETEIMG-MIB", rlDeleteImgKey=rlDeleteImgKey, rlDeleteImgEntry=rlDeleteImgEntry, rlDeleteImg=rlDeleteImg, DELETEIMGName=DELETEIMGName, rlDeleteImgName=rlDeleteImgName, rlDeleteImgUnit=rlDeleteImgUnit, PYSNMP_MODULE_ID=rlDeleteImg, rlDeleteImgTable=rlDeleteImgTable)
