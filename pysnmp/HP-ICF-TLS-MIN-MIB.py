#
# PySNMP MIB module HP-ICF-TLS-MIN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-TLS-MIN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:23:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
NotificationType, ObjectIdentity, Unsigned32, Counter32, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, iso, TimeTicks, ModuleIdentity, Gauge32, Counter64, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "Unsigned32", "Counter32", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "iso", "TimeTicks", "ModuleIdentity", "Gauge32", "Counter64", "Bits")
TextualConvention, RowStatus, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString", "TruthValue")
hpicfTlsMinMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112))
hpicfTlsMinMIB.setRevisions(('2017-05-11 09:00', '2017-04-05 09:00', '2016-06-22 09:00', '2014-10-01 09:00',))
if mibBuilder.loadTexts: hpicfTlsMinMIB.setLastUpdated('201705110900Z')
if mibBuilder.loadTexts: hpicfTlsMinMIB.setOrganization('HP Networking')
hpicfTlsMinObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0))
hpicfTlsMinConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1))
hpicfTlsMinConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1))
hpicfTlsMinTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 1), )
if mibBuilder.loadTexts: hpicfTlsMinTable.setStatus('current')
hpicfTlsMinEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 1, 1), ).setIndexNames((0, "HP-ICF-TLS-MIN-MIB", "hpicfTlsMinApp"))
if mibBuilder.loadTexts: hpicfTlsMinEntry.setStatus('current')
hpicfTlsMinApp = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("webSsl", 1), ("openflow", 2), ("syslog", 3), ("tr69", 4), ("cloud", 5))))
if mibBuilder.loadTexts: hpicfTlsMinApp.setStatus('current')
hpicfTlsMinVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("tls1dot0", 1), ("tls1dot1", 2), ("tls1dot2", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfTlsMinVersion.setStatus('current')
hpicfTlsMinCloseSSLSess = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 1, 1, 3), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfTlsMinCloseSSLSess.setStatus('current')
hpicfTlsMinRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfTlsMinRowStatus.setStatus('current')
hpicfTlsMinCipherTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 2), )
if mibBuilder.loadTexts: hpicfTlsMinCipherTable.setStatus('current')
hpicfTlsMinCipherEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 2, 1), ).setIndexNames((0, "HP-ICF-TLS-MIN-MIB", "hpicfTlsMinApp"), (0, "HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCipher"))
if mibBuilder.loadTexts: hpicfTlsMinCipherEntry.setStatus('current')
hpicfTlsMinCipher = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36))).clone(namedValues=NamedValues(("aes256Sha256", 1), ("aes256Sha", 2), ("aes128Sha256", 3), ("aes128Sha", 4), ("des3CbcSha", 5), ("aes256GcmSha384", 6), ("aes128GcmSha256", 7), ("ecdhEcdsaAes256GcmSha384", 8), ("ecdhRsaAaes256GcmSha384", 9), ("ecdhEcdsaAes128GcmSha256", 10), ("ecdhRsaAes128GcmSha256", 11), ("ecdhEcdsaAes256Sha384", 12), ("ecdhRsaAes256Sha384", 13), ("ecdhEcdsaAes256Sha", 14), ("ecdhRsaAes256Sha", 15), ("ecdhEcdsaAes128Sha256", 16), ("ecdhRsaAes128Sha256", 17), ("ecdhEcdsaAes128Sha", 18), ("ecdhRsaAes128Sha", 19), ("ecdhEcdsaDesCbc3Sha", 20), ("ecdhRsaDesCbc3Sha", 21), ("ecdheEcdsaAes128GcmSha256", 22), ("ecdheRsaAes128GcmSha256", 23), ("ecdheEcdsaAes128Sha256", 24), ("ecdheRsaAes128Sha256", 25), ("ecdheEcdsaAes128Sha", 26), ("ecdheRsaAes128Sha", 27), ("ecdheEcdsaAes256GcmSha384", 28), ("ecdheRsaAes256GcmSha384", 29), ("ecdheEcdsaAes256Sha384", 30), ("ecdheRsaAes256Sha384", 31), ("ecdheEcdsaAes256Sha", 32), ("ecdheRsaAes256Sha", 33), ("ecdheEcdsaDesCbc3Sha", 34), ("ecdheRsaDesCbc3Sha", 35), ("all", 36))))
if mibBuilder.loadTexts: hpicfTlsMinCipher.setStatus('current')
hpicfTlsMinCipherRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfTlsMinCipherRowStatus.setStatus('current')
hpicfTlsMinCipherConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enforce", 1), ("disable", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfTlsMinCipherConfig.setStatus('current')
hpicfTlsMinCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1, 1))
hpicfTlsMinGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1, 2))
hpicfTlsMinCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1, 1, 1)).setObjects(("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfTlsMinCompliance1 = hpicfTlsMinCompliance1.setStatus('deprecated')
hpicfTlsMinConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1, 2, 1)).setObjects(("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinVersion"), ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCloseSSLSess"), ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinRowStatus"), ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCipherRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfTlsMinConfigGroup = hpicfTlsMinConfigGroup.setStatus('deprecated')
hpicfTlsMinCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1, 1, 2)).setObjects(("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinConfigGroup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfTlsMinCompliance2 = hpicfTlsMinCompliance2.setStatus('deprecated')
hpicfTlsMinConfigGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1, 2, 2)).setObjects(("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinVersion"), ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCloseSSLSess"), ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinRowStatus"), ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCipherRowStatus"), ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCipherConfig"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfTlsMinConfigGroup1 = hpicfTlsMinConfigGroup1.setStatus('deprecated')
hpicfTlsMinCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1, 1, 3)).setObjects(("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinConfigGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfTlsMinCompliance3 = hpicfTlsMinCompliance3.setStatus('current')
hpicfTlsMinConfigGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1, 2, 3)).setObjects(("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinVersion"), ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCloseSSLSess"), ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinRowStatus"), ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCipherRowStatus"), ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCipherConfig"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfTlsMinConfigGroup2 = hpicfTlsMinConfigGroup2.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-TLS-MIN-MIB", hpicfTlsMinCipherConfig=hpicfTlsMinCipherConfig, hpicfTlsMinEntry=hpicfTlsMinEntry, hpicfTlsMinConfigGroup=hpicfTlsMinConfigGroup, hpicfTlsMinCipherTable=hpicfTlsMinCipherTable, hpicfTlsMinConfigGroup1=hpicfTlsMinConfigGroup1, PYSNMP_MODULE_ID=hpicfTlsMinMIB, hpicfTlsMinConformance=hpicfTlsMinConformance, hpicfTlsMinCompliances=hpicfTlsMinCompliances, hpicfTlsMinConfigGroup2=hpicfTlsMinConfigGroup2, hpicfTlsMinGroups=hpicfTlsMinGroups, hpicfTlsMinObjects=hpicfTlsMinObjects, hpicfTlsMinCompliance2=hpicfTlsMinCompliance2, hpicfTlsMinCompliance3=hpicfTlsMinCompliance3, hpicfTlsMinCipherEntry=hpicfTlsMinCipherEntry, hpicfTlsMinTable=hpicfTlsMinTable, hpicfTlsMinCipher=hpicfTlsMinCipher, hpicfTlsMinConfigObjects=hpicfTlsMinConfigObjects, hpicfTlsMinCipherRowStatus=hpicfTlsMinCipherRowStatus, hpicfTlsMinApp=hpicfTlsMinApp, hpicfTlsMinVersion=hpicfTlsMinVersion, hpicfTlsMinCompliance1=hpicfTlsMinCompliance1, hpicfTlsMinCloseSSLSess=hpicfTlsMinCloseSSLSess, hpicfTlsMinMIB=hpicfTlsMinMIB, hpicfTlsMinRowStatus=hpicfTlsMinRowStatus)
