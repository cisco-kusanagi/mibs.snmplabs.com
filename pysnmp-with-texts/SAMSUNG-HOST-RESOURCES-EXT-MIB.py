#
# PySNMP MIB module SAMSUNG-HOST-RESOURCES-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SAMSUNG-HOST-RESOURCES-EXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:00:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
hrDeviceIndex, = mibBuilder.importSymbols("HOST-RESOURCES-MIB", "hrDeviceIndex")
samsungCommonMIB, = mibBuilder.importSymbols("SAMSUNG-COMMON-MIB", "samsungCommonMIB")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Counter32, Integer32, Bits, NotificationType, Unsigned32, MibIdentifier, IpAddress, TimeTicks, Gauge32, ObjectIdentity, iso, ModuleIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Integer32", "Bits", "NotificationType", "Unsigned32", "MibIdentifier", "IpAddress", "TimeTicks", "Gauge32", "ObjectIdentity", "iso", "ModuleIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
scmHrMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53))
if mibBuilder.loadTexts: scmHrMIB.setLastUpdated('190407170000Z')
if mibBuilder.loadTexts: scmHrMIB.setOrganization('Samsung Corporation - SCMI Working Group')
if mibBuilder.loadTexts: scmHrMIB.setContactInfo(' SCMI Editors Email: coherence@crt.samsung.com -- -- ')
if mibBuilder.loadTexts: scmHrMIB.setDescription("Version: 1.00 The MIB module for extended configuration and management of various host resources for network accessible host systems. This module augments and extends the original IETF Host Resources MIB (RFC 2790). Usage: This MIB module introduces support for the 'realization' of both 'physical' and 'logical' devices, consistent with the Document Printing Application (DPA), ISO/IEC 10175, as reflected in the object 'scmHrDevInfoRealization'. Note: Conforming implementations SHALL NOT 'bubble up' status from 'physical' devices to associated 'logical' devices. All devices SHALL report their own status ONLY. See: Section 9 'Supplement' in SCMI Extensions to IETF Host Resources TC, for implementation guidance for this MIB module. Copyright (C) 1995-2002 Samsung Corporation. All Rights Reserved.")
class ScmHrDevCountJobTypeTC(TextualConvention, Integer32):
    description = 'The type of count job.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 11, 12, 21))
    namedValues = NamedValues(("print", 1), ("copy", 2), ("faxIn", 3), ("faxOut", 4), ("scan", 5), ("report", 6), ("digitalSend", 11), ("digitalRecieve", 12), ("localStorage", 21))

class ScmHrDevCountMediaSizeTC(TextualConvention, Integer32):
    description = 'The size of media.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32))
    namedValues = NamedValues(("small", 1), ("large", 2), ("letter", 3), ("legal", 4), ("a4", 5), ("executive", 6), ("jisB5", 7), ("isoB5", 8), ("com10", 9), ("monarch", 10), ("dl", 11), ("c5", 12), ("postA6", 13), ("c6", 14), ("folio", 15), ("a5", 16), ("statement", 17), ("a6", 18), ("ledger", 19), ("a3", 20), ("jisB4", 21), ("jpost", 22), ("jpostd", 23), ("custom", 24), ("letterP", 25), ("a4P", 26), ("jisB5P", 27), ("a5P", 28), ("executiveP", 29), ("statementP", 30), ("a3Over", 31), ("b5Envelope", 32))

class ScmHrDevCountUnitTC(TextualConvention, Integer32):
    description = 'The count unit of job count.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 7, 8, 11, 12, 13, 14, 15, 16, 17, 18, 19))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("tenThousandthsOfInches", 3), ("micrometers", 4), ("impressions", 7), ("sheets", 8), ("hours", 11), ("thousandthsOfOunces", 12), ("tenthsOfGrams", 13), ("hundrethsOfFluidOunces", 14), ("tenthsOfMilliliters", 15), ("feet", 16), ("meters", 17), ("items", 18), ("percent", 19))

class ScmHrDevCountDuplexTC(TextualConvention, Integer32):
    description = 'The duplex type of job'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("simplex", 1), ("duplex", 2), ("duplexSingle", 3))

class ScmHrDevCountColorTC(TextualConvention, Integer32):
    description = 'The color type of job'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("fullColor", 1), ("singleColor", 2), ("monoColor", 3))

scmHrMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 2))
scmHrMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 2, 2))
scmHrDevInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 2, 2, 3)).setObjects(("SAMSUNG-HOST-RESOURCES-EXT-MIB", "scmHrDevCountIndex"), ("SAMSUNG-HOST-RESOURCES-EXT-MIB", "scmHrDevCountJobType"), ("SAMSUNG-HOST-RESOURCES-EXT-MIB", "scmHrDevCountMediaSize"), ("SAMSUNG-HOST-RESOURCES-EXT-MIB", "scmHrDevCountUnit"), ("SAMSUNG-HOST-RESOURCES-EXT-MIB", "scmHrDevCountDuplex"), ("SAMSUNG-HOST-RESOURCES-EXT-MIB", "scmHrDevCountColor"), ("SAMSUNG-HOST-RESOURCES-EXT-MIB", "scmHrDevCountValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    scmHrDevInfoGroup = scmHrDevInfoGroup.setStatus('current')
if mibBuilder.loadTexts: scmHrDevInfoGroup.setDescription('The Host Resources Extensions MIB Device Info Group')
scmHrDevCount = MibIdentifier((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 11))
scmHrDevCountSimple = MibIdentifier((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 11, 1))
scmHrDevCountTable = MibTable((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 11, 2), )
if mibBuilder.loadTexts: scmHrDevCountTable.setStatus('current')
if mibBuilder.loadTexts: scmHrDevCountTable.setDescription('Samsung Common Mib Host Resource Count MIB ')
scmHrDevCountEntry = MibTableRow((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 11, 2, 1), ).setIndexNames((0, "HOST-RESOURCES-MIB", "hrDeviceIndex"), (0, "SAMSUNG-HOST-RESOURCES-EXT-MIB", "scmHrDevCountIndex"))
if mibBuilder.loadTexts: scmHrDevCountEntry.setReference("See: 'prtAlertEntry' in the Printer MIB.")
if mibBuilder.loadTexts: scmHrDevCountEntry.setStatus('current')
if mibBuilder.loadTexts: scmHrDevCountEntry.setDescription('An entry for a device alert which has been generated and recorded on this host system.')
scmHrDevCountIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 11, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: scmHrDevCountIndex.setStatus('current')
if mibBuilder.loadTexts: scmHrDevCountIndex.setDescription('A unique value used by the host to identify this Count item. This value indicate index of usage count value. If host device supports three count value (total page count, total color print count, total mono print count), this device has three count value and index.')
scmHrDevCountJobType = MibTableColumn((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 11, 2, 1, 2), ScmHrDevCountJobTypeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scmHrDevCountJobType.setReference(' ')
if mibBuilder.loadTexts: scmHrDevCountJobType.setStatus('current')
if mibBuilder.loadTexts: scmHrDevCountJobType.setDescription('scmHrDevCount defines items that are outside of the normal numeric range: other(-1), unknown(-2). scm defines many a job type. but current samsung device supports counts of print, fax, copy and scan job. Thus, the other items is not used. ')
scmHrDevCountMediaSize = MibTableColumn((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 11, 2, 1, 3), ScmHrDevCountMediaSizeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scmHrDevCountMediaSize.setStatus('current')
if mibBuilder.loadTexts: scmHrDevCountMediaSize.setDescription("smcHrDevCount defines items that are outside of the normal numeric range: other(-1), unknown(-2). scm defines many a size of media. But, We use 'small' or 'large' as media size so that application simply manage. ")
scmHrDevCountUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 11, 2, 1, 4), ScmHrDevCountUnitTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scmHrDevCountUnit.setStatus('current')
if mibBuilder.loadTexts: scmHrDevCountUnit.setDescription('smcHrDevCount define items that are outside of the normal numeric range: other(-1), unknown(-2). PWG define count unit in printer mib(RFC1759, RFC3805). Default value is sheet(8), but specifically use impression (for example OEM Model).')
scmHrDevCountDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 11, 2, 1, 5), ScmHrDevCountDuplexTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scmHrDevCountDuplex.setStatus('current')
if mibBuilder.loadTexts: scmHrDevCountDuplex.setDescription('smcHrDevCount define items that are outside of the normal numeric range: other(-1), unknown(-2). samsung device suppor three duplex job type, simple, duplex, duplex(single). ')
scmHrDevCountColor = MibTableColumn((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 11, 2, 1, 6), ScmHrDevCountColorTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scmHrDevCountColor.setReference('smcHrDevCount define items that are outside of the normal numeric range: other(-1), unknown(-2).')
if mibBuilder.loadTexts: scmHrDevCountColor.setStatus('current')
if mibBuilder.loadTexts: scmHrDevCountColor.setDescription('smcHrDevCount define items that are outside of the normal numeric range: other(-1), unknown(-2). single-color is defined for extension of color job count.')
scmHrDevCountValue = MibTableColumn((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 11, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: scmHrDevCountValue.setStatus('current')
if mibBuilder.loadTexts: scmHrDevCountValue.setDescription('Value of usage count.')
mibBuilder.exportSymbols("SAMSUNG-HOST-RESOURCES-EXT-MIB", scmHrDevCount=scmHrDevCount, scmHrDevCountTable=scmHrDevCountTable, ScmHrDevCountJobTypeTC=ScmHrDevCountJobTypeTC, scmHrDevCountEntry=scmHrDevCountEntry, scmHrDevCountDuplex=scmHrDevCountDuplex, ScmHrDevCountColorTC=ScmHrDevCountColorTC, PYSNMP_MODULE_ID=scmHrMIB, scmHrDevCountSimple=scmHrDevCountSimple, scmHrMIBGroups=scmHrMIBGroups, ScmHrDevCountDuplexTC=ScmHrDevCountDuplexTC, scmHrDevCountJobType=scmHrDevCountJobType, scmHrDevCountUnit=scmHrDevCountUnit, scmHrDevInfoGroup=scmHrDevInfoGroup, scmHrDevCountValue=scmHrDevCountValue, scmHrDevCountColor=scmHrDevCountColor, scmHrMIBConformance=scmHrMIBConformance, ScmHrDevCountMediaSizeTC=ScmHrDevCountMediaSizeTC, scmHrDevCountMediaSize=scmHrDevCountMediaSize, scmHrMIB=scmHrMIB, scmHrDevCountIndex=scmHrDevCountIndex, ScmHrDevCountUnitTC=ScmHrDevCountUnitTC)
