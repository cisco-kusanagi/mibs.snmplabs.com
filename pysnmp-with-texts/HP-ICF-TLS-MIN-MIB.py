#
# PySNMP MIB module HP-ICF-TLS-MIN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-TLS-MIN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:35:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, Unsigned32, ModuleIdentity, NotificationType, Integer32, TimeTicks, Counter64, MibIdentifier, ObjectIdentity, iso, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "Unsigned32", "ModuleIdentity", "NotificationType", "Integer32", "TimeTicks", "Counter64", "MibIdentifier", "ObjectIdentity", "iso", "Bits", "IpAddress")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
hpicfTlsMinMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112))
hpicfTlsMinMIB.setRevisions(('2017-05-11 09:00', '2017-04-05 09:00', '2016-06-22 09:00', '2014-10-01 09:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpicfTlsMinMIB.setRevisionsDescriptions(('Modified cipher names listed for hpicfTlsMinCipher.', 'Added new mib object hpicfTlsMinCipherConfig in hpicfTlsMinCipherTable to enforce or disable cipher. Modified index values allowed for hpicfTlsMinCipher.', 'Added new app type cloud to hpicfTlsMinApp.', 'Initial version of TLS Minimum MIB module.',))
if mibBuilder.loadTexts: hpicfTlsMinMIB.setLastUpdated('201705110900Z')
if mibBuilder.loadTexts: hpicfTlsMinMIB.setOrganization('HP Networking')
if mibBuilder.loadTexts: hpicfTlsMinMIB.setContactInfo('Hewlett-Packard Enterprise Company 8000 Foothills Blvd. Roseville, CA 95747')
if mibBuilder.loadTexts: hpicfTlsMinMIB.setDescription('This MIB module describes objects for enforcing TLS minimum version enforcement and ciphersuire enforcement in the HP Integrated Communication Facility product line.')
hpicfTlsMinObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0))
hpicfTlsMinConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1))
hpicfTlsMinConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1))
hpicfTlsMinTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 1), )
if mibBuilder.loadTexts: hpicfTlsMinTable.setStatus('current')
if mibBuilder.loadTexts: hpicfTlsMinTable.setDescription('A table of minimum TLS version objects')
hpicfTlsMinEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 1, 1), ).setIndexNames((0, "HP-ICF-TLS-MIN-MIB", "hpicfTlsMinApp"))
if mibBuilder.loadTexts: hpicfTlsMinEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfTlsMinEntry.setDescription('An entry in the hpicfTlsMinTable.')
hpicfTlsMinApp = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("webSsl", 1), ("openflow", 2), ("syslog", 3), ("tr69", 4), ("cloud", 5))))
if mibBuilder.loadTexts: hpicfTlsMinApp.setStatus('current')
if mibBuilder.loadTexts: hpicfTlsMinApp.setDescription('This object specifies the application for which the minimum TLS version and cipher suite is enforced.')
hpicfTlsMinVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("tls1dot0", 1), ("tls1dot1", 2), ("tls1dot2", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfTlsMinVersion.setStatus('current')
if mibBuilder.loadTexts: hpicfTlsMinVersion.setDescription('This object specifies the minimum TLS version enforced. The default value for this attribute will be TLS1.1')
hpicfTlsMinCloseSSLSess = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 1, 1, 3), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfTlsMinCloseSSLSess.setStatus('current')
if mibBuilder.loadTexts: hpicfTlsMinCloseSSLSess.setDescription('This object specifies whether or not to close existing SSL sessions. Setting this attribute to TRUE will close all existing SSL sessions. Setting this attribute to FALSE will not have any effect.')
hpicfTlsMinRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfTlsMinRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpicfTlsMinRowStatus.setDescription('Status of this row, by which new entries may be created or existing entries deleted from this table.')
hpicfTlsMinCipherTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 2), )
if mibBuilder.loadTexts: hpicfTlsMinCipherTable.setStatus('current')
if mibBuilder.loadTexts: hpicfTlsMinCipherTable.setDescription('A table that contains a list of cipher suites that can be enforced or disabled for various applications.')
hpicfTlsMinCipherEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 2, 1), ).setIndexNames((0, "HP-ICF-TLS-MIN-MIB", "hpicfTlsMinApp"), (0, "HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCipher"))
if mibBuilder.loadTexts: hpicfTlsMinCipherEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfTlsMinCipherEntry.setDescription('An entry in the hpicfTlsMinTable that lists the lowest TLS version and cipher suites enforced or disabled for each application.')
hpicfTlsMinCipher = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36))).clone(namedValues=NamedValues(("aes256Sha256", 1), ("aes256Sha", 2), ("aes128Sha256", 3), ("aes128Sha", 4), ("des3CbcSha", 5), ("aes256GcmSha384", 6), ("aes128GcmSha256", 7), ("ecdhEcdsaAes256GcmSha384", 8), ("ecdhRsaAaes256GcmSha384", 9), ("ecdhEcdsaAes128GcmSha256", 10), ("ecdhRsaAes128GcmSha256", 11), ("ecdhEcdsaAes256Sha384", 12), ("ecdhRsaAes256Sha384", 13), ("ecdhEcdsaAes256Sha", 14), ("ecdhRsaAes256Sha", 15), ("ecdhEcdsaAes128Sha256", 16), ("ecdhRsaAes128Sha256", 17), ("ecdhEcdsaAes128Sha", 18), ("ecdhRsaAes128Sha", 19), ("ecdhEcdsaDesCbc3Sha", 20), ("ecdhRsaDesCbc3Sha", 21), ("ecdheEcdsaAes128GcmSha256", 22), ("ecdheRsaAes128GcmSha256", 23), ("ecdheEcdsaAes128Sha256", 24), ("ecdheRsaAes128Sha256", 25), ("ecdheEcdsaAes128Sha", 26), ("ecdheRsaAes128Sha", 27), ("ecdheEcdsaAes256GcmSha384", 28), ("ecdheRsaAes256GcmSha384", 29), ("ecdheEcdsaAes256Sha384", 30), ("ecdheRsaAes256Sha384", 31), ("ecdheEcdsaAes256Sha", 32), ("ecdheRsaAes256Sha", 33), ("ecdheEcdsaDesCbc3Sha", 34), ("ecdheRsaDesCbc3Sha", 35), ("all", 36))))
if mibBuilder.loadTexts: hpicfTlsMinCipher.setStatus('current')
if mibBuilder.loadTexts: hpicfTlsMinCipher.setDescription('This object specifies the cipher suite enforced for applications.')
hpicfTlsMinCipherRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfTlsMinCipherRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpicfTlsMinCipherRowStatus.setDescription('Status of this row, by which new entries may be created or existing entries deleted from this table.')
hpicfTlsMinCipherConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enforce", 1), ("disable", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfTlsMinCipherConfig.setStatus('current')
if mibBuilder.loadTexts: hpicfTlsMinCipherConfig.setDescription('This object has to be configured to enforce or disable cipher suite for applications.')
hpicfTlsMinCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1, 1))
hpicfTlsMinGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1, 2))
hpicfTlsMinCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1, 1, 1)).setObjects(("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfTlsMinCompliance1 = hpicfTlsMinCompliance1.setStatus('deprecated')
if mibBuilder.loadTexts: hpicfTlsMinCompliance1.setDescription('The compliance statement')
hpicfTlsMinConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1, 2, 1)).setObjects(("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinVersion"), ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCloseSSLSess"), ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinRowStatus"), ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCipherRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfTlsMinConfigGroup = hpicfTlsMinConfigGroup.setStatus('deprecated')
if mibBuilder.loadTexts: hpicfTlsMinConfigGroup.setDescription('A collection of objects providing configuration for TLS minimum version and cipher suite enforcement for an app.')
hpicfTlsMinCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1, 1, 2)).setObjects(("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinConfigGroup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfTlsMinCompliance2 = hpicfTlsMinCompliance2.setStatus('deprecated')
if mibBuilder.loadTexts: hpicfTlsMinCompliance2.setDescription('The compliance statement')
hpicfTlsMinConfigGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1, 2, 2)).setObjects(("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinVersion"), ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCloseSSLSess"), ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinRowStatus"), ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCipherRowStatus"), ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCipherConfig"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfTlsMinConfigGroup1 = hpicfTlsMinConfigGroup1.setStatus('deprecated')
if mibBuilder.loadTexts: hpicfTlsMinConfigGroup1.setDescription('A collection of objects providing configuration for TLS minimum version and cipher suite enforcement for an app.')
hpicfTlsMinCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1, 1, 3)).setObjects(("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinConfigGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfTlsMinCompliance3 = hpicfTlsMinCompliance3.setStatus('current')
if mibBuilder.loadTexts: hpicfTlsMinCompliance3.setDescription('The compliance statement')
hpicfTlsMinConfigGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1, 2, 3)).setObjects(("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinVersion"), ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCloseSSLSess"), ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinRowStatus"), ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCipherRowStatus"), ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCipherConfig"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfTlsMinConfigGroup2 = hpicfTlsMinConfigGroup2.setStatus('current')
if mibBuilder.loadTexts: hpicfTlsMinConfigGroup2.setDescription('A collection of objects providing configuration for TLS minimum version and cipher suite enforcement for an app.')
mibBuilder.exportSymbols("HP-ICF-TLS-MIN-MIB", hpicfTlsMinTable=hpicfTlsMinTable, hpicfTlsMinApp=hpicfTlsMinApp, hpicfTlsMinCipherConfig=hpicfTlsMinCipherConfig, hpicfTlsMinCompliance2=hpicfTlsMinCompliance2, hpicfTlsMinCompliance3=hpicfTlsMinCompliance3, hpicfTlsMinEntry=hpicfTlsMinEntry, hpicfTlsMinCipher=hpicfTlsMinCipher, hpicfTlsMinCipherRowStatus=hpicfTlsMinCipherRowStatus, hpicfTlsMinCompliance1=hpicfTlsMinCompliance1, hpicfTlsMinCipherTable=hpicfTlsMinCipherTable, hpicfTlsMinCompliances=hpicfTlsMinCompliances, PYSNMP_MODULE_ID=hpicfTlsMinMIB, hpicfTlsMinConfigGroup1=hpicfTlsMinConfigGroup1, hpicfTlsMinCloseSSLSess=hpicfTlsMinCloseSSLSess, hpicfTlsMinCipherEntry=hpicfTlsMinCipherEntry, hpicfTlsMinGroups=hpicfTlsMinGroups, hpicfTlsMinRowStatus=hpicfTlsMinRowStatus, hpicfTlsMinMIB=hpicfTlsMinMIB, hpicfTlsMinObjects=hpicfTlsMinObjects, hpicfTlsMinConfigGroup=hpicfTlsMinConfigGroup, hpicfTlsMinConfigObjects=hpicfTlsMinConfigObjects, hpicfTlsMinConformance=hpicfTlsMinConformance, hpicfTlsMinConfigGroup2=hpicfTlsMinConfigGroup2, hpicfTlsMinVersion=hpicfTlsMinVersion)
