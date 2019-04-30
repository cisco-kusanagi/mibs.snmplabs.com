#
# PySNMP MIB module TPT-LICENSE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPT-LICENSE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:18:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, NotificationType, Gauge32, IpAddress, MibIdentifier, Bits, Counter32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, iso, ObjectIdentity, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "Gauge32", "IpAddress", "MibIdentifier", "Bits", "Counter32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "iso", "ObjectIdentity", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tpt_tpa_objs, = mibBuilder.importSymbols("TPT-TPAMIBS-MIB", "tpt-tpa-objs")
tpt_license_objs = ModuleIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 15)).setLabel("tpt-license-objs")
tpt_license_objs.setRevisions(('2016-05-25 18:54',))
if mibBuilder.loadTexts: tpt_license_objs.setLastUpdated('201605251854Z')
if mibBuilder.loadTexts: tpt_license_objs.setOrganization('Trend Micro, Inc.')
class LicenseStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("info", 0), ("ok", 1), ("warning", 2), ("error", 3))

class LicenseAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("allow", 0), ("deny", 1))

licenseTable = MibTable((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 15, 1), )
if mibBuilder.loadTexts: licenseTable.setStatus('current')
licenseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 15, 1, 1), ).setIndexNames((0, "TPT-LICENSE-MIB", "licenseEntryIndex"))
if mibBuilder.loadTexts: licenseEntry.setStatus('current')
licenseEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 15, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: licenseEntryIndex.setStatus('current')
licenseEntryFeature = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 15, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: licenseEntryFeature.setStatus('current')
licenseEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 15, 1, 1, 3), LicenseStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: licenseEntryStatus.setStatus('current')
licenseEntryAction = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 15, 1, 1, 4), LicenseAction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: licenseEntryAction.setStatus('current')
licenseEntryExpiry = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 15, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: licenseEntryExpiry.setStatus('current')
licenseEntryDetails = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 15, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: licenseEntryDetails.setStatus('current')
mibBuilder.exportSymbols("TPT-LICENSE-MIB", licenseEntryAction=licenseEntryAction, licenseEntryDetails=licenseEntryDetails, LicenseAction=LicenseAction, PYSNMP_MODULE_ID=tpt_license_objs, licenseEntryIndex=licenseEntryIndex, LicenseStatus=LicenseStatus, licenseEntryFeature=licenseEntryFeature, licenseEntry=licenseEntry, licenseEntryStatus=licenseEntryStatus, tpt_license_objs=tpt_license_objs, licenseEntryExpiry=licenseEntryExpiry, licenseTable=licenseTable)
