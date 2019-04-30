#
# PySNMP MIB module DOCS-BPI2EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DOCS-BPI2EXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:37:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
clabProjDocsis, = mibBuilder.importSymbols("CLAB-DEF-MIB", "clabProjDocsis")
DocsX509ASN1DEREncodedCertificate, = mibBuilder.importSymbols("DOCS-IETF-BPI2-MIB", "DocsX509ASN1DEREncodedCertificate")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
TimeTicks, ObjectIdentity, Bits, Counter32, Unsigned32, iso, Gauge32, MibIdentifier, Integer32, Counter64, IpAddress, NotificationType, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "Bits", "Counter32", "Unsigned32", "iso", "Gauge32", "MibIdentifier", "Integer32", "Counter64", "IpAddress", "NotificationType", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
docsBpi2Ext31Mib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4491, 2, 1, 29))
docsBpi2Ext31Mib.setRevisions(('2017-04-13 00:00', '2016-10-20 00:00', '2016-05-05 00:00', '2016-01-13 00:00',))
if mibBuilder.loadTexts: docsBpi2Ext31Mib.setLastUpdated('201704130000Z')
if mibBuilder.loadTexts: docsBpi2Ext31Mib.setOrganization('Cable Television Laboratories, Inc.')
class DocsCvcCaCertificateChain(TextualConvention, OctetString):
    status = 'current'
    displayHint = '50x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 8192)

docsBpi2Ext31Notifications = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 0))
docsBpi2Ext31MibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 1))
docsBpi2Ext31Conformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 2))
docsBpi2Ext31Compliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 2, 1))
docsBpi2Ext31Groups = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 2, 2))
docsBpi2Ext31CmObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 1, 1))
docsBpi2Ext31CmCertObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 1, 1, 1))
docsBpi2Ext31CodeDownloadControl = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 1, 2))
docsBpi2Ext31CmDeviceCertTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 1, 1, 1, 1), )
if mibBuilder.loadTexts: docsBpi2Ext31CmDeviceCertTable.setStatus('current')
docsBpi2Ext31CmDeviceCertEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 1, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: docsBpi2Ext31CmDeviceCertEntry.setStatus('current')
docsBpi2Ext31CmDeviceCmCert = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 1, 1, 1, 1, 1, 1), DocsX509ASN1DEREncodedCertificate()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsBpi2Ext31CmDeviceCmCert.setStatus('current')
docsBpi2Ext31CmDeviceManufCert = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 1, 1, 1, 1, 1, 2), DocsX509ASN1DEREncodedCertificate()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsBpi2Ext31CmDeviceManufCert.setStatus('current')
docsBpi2Ext31CodeUpdateCvcChain = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 1, 2, 1), DocsCvcCaCertificateChain()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsBpi2Ext31CodeUpdateCvcChain.setStatus('current')
docsBpi2Ext31CodeMfgOrgName = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 1, 2, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsBpi2Ext31CodeMfgOrgName.setStatus('current')
docsBpi2Ext31CodeMfgCodeAccessStart = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 1, 2, 3), DateAndTime().subtype(subtypeSpec=ValueSizeConstraint(11, 11)).setFixedLength(11)).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsBpi2Ext31CodeMfgCodeAccessStart.setStatus('current')
docsBpi2Ext31CodeMfgCvcAccessStart = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 1, 2, 4), DateAndTime().subtype(subtypeSpec=ValueSizeConstraint(11, 11)).setFixedLength(11)).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsBpi2Ext31CodeMfgCvcAccessStart.setStatus('current')
docsBpi2Ext31CodeCoSignerOrgName = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 1, 2, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsBpi2Ext31CodeCoSignerOrgName.setStatus('current')
docsBpi2Ext31CodeCoSignerCodeAccessStart = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 1, 2, 6), DateAndTime().subtype(subtypeSpec=ValueSizeConstraint(11, 11)).setFixedLength(11)).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsBpi2Ext31CodeCoSignerCodeAccessStart.setStatus('current')
docsBpi2Ext31CodeCoSignerCvcAccessStart = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 1, 2, 7), DateAndTime().subtype(subtypeSpec=ValueSizeConstraint(11, 11)).setFixedLength(11)).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsBpi2Ext31CodeCoSignerCvcAccessStart.setStatus('current')
docsBpi2Ext31MIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 2, 1, 1)).setObjects(("DOCS-BPI2EXT-MIB", "docsBpi2Ext31CmGroup"), ("DOCS-BPI2EXT-MIB", "docsBpi2Ext31BaseGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsBpi2Ext31MIBCompliance = docsBpi2Ext31MIBCompliance.setStatus('current')
docsBpi2Ext31CmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 2, 2, 1)).setObjects(("DOCS-BPI2EXT-MIB", "docsBpi2Ext31CmDeviceCmCert"), ("DOCS-BPI2EXT-MIB", "docsBpi2Ext31CmDeviceManufCert"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsBpi2Ext31CmGroup = docsBpi2Ext31CmGroup.setStatus('current')
docsBpi2Ext31BaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4491, 2, 1, 29, 2, 2, 2)).setObjects(("DOCS-BPI2EXT-MIB", "docsBpi2Ext31CodeUpdateCvcChain"), ("DOCS-BPI2EXT-MIB", "docsBpi2Ext31CodeMfgOrgName"), ("DOCS-BPI2EXT-MIB", "docsBpi2Ext31CodeMfgCodeAccessStart"), ("DOCS-BPI2EXT-MIB", "docsBpi2Ext31CodeMfgCvcAccessStart"), ("DOCS-BPI2EXT-MIB", "docsBpi2Ext31CodeCoSignerOrgName"), ("DOCS-BPI2EXT-MIB", "docsBpi2Ext31CodeCoSignerCodeAccessStart"), ("DOCS-BPI2EXT-MIB", "docsBpi2Ext31CodeCoSignerCvcAccessStart"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsBpi2Ext31BaseGroup = docsBpi2Ext31BaseGroup.setStatus('current')
mibBuilder.exportSymbols("DOCS-BPI2EXT-MIB", docsBpi2Ext31Notifications=docsBpi2Ext31Notifications, docsBpi2Ext31BaseGroup=docsBpi2Ext31BaseGroup, docsBpi2Ext31Mib=docsBpi2Ext31Mib, PYSNMP_MODULE_ID=docsBpi2Ext31Mib, docsBpi2Ext31CodeUpdateCvcChain=docsBpi2Ext31CodeUpdateCvcChain, docsBpi2Ext31CmDeviceCertTable=docsBpi2Ext31CmDeviceCertTable, docsBpi2Ext31CmGroup=docsBpi2Ext31CmGroup, docsBpi2Ext31CodeMfgCodeAccessStart=docsBpi2Ext31CodeMfgCodeAccessStart, docsBpi2Ext31Compliances=docsBpi2Ext31Compliances, docsBpi2Ext31CmCertObjects=docsBpi2Ext31CmCertObjects, docsBpi2Ext31MibObjects=docsBpi2Ext31MibObjects, docsBpi2Ext31CodeMfgCvcAccessStart=docsBpi2Ext31CodeMfgCvcAccessStart, docsBpi2Ext31CmObjects=docsBpi2Ext31CmObjects, docsBpi2Ext31CmDeviceCmCert=docsBpi2Ext31CmDeviceCmCert, docsBpi2Ext31CodeMfgOrgName=docsBpi2Ext31CodeMfgOrgName, docsBpi2Ext31CodeCoSignerCvcAccessStart=docsBpi2Ext31CodeCoSignerCvcAccessStart, docsBpi2Ext31MIBCompliance=docsBpi2Ext31MIBCompliance, docsBpi2Ext31CmDeviceCertEntry=docsBpi2Ext31CmDeviceCertEntry, DocsCvcCaCertificateChain=DocsCvcCaCertificateChain, docsBpi2Ext31Conformance=docsBpi2Ext31Conformance, docsBpi2Ext31CodeCoSignerOrgName=docsBpi2Ext31CodeCoSignerOrgName, docsBpi2Ext31CmDeviceManufCert=docsBpi2Ext31CmDeviceManufCert, docsBpi2Ext31Groups=docsBpi2Ext31Groups, docsBpi2Ext31CodeCoSignerCodeAccessStart=docsBpi2Ext31CodeCoSignerCodeAccessStart, docsBpi2Ext31CodeDownloadControl=docsBpi2Ext31CodeDownloadControl)
