#
# PySNMP MIB module MGMT-SECURITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MGMT-SECURITY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:11:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
quanta, switch = mibBuilder.importSymbols("QUANTA-SWITCH-MIB", "quanta", "switch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter64, iso, TimeTicks, Integer32, Unsigned32, NotificationType, IpAddress, ModuleIdentity, Bits, Gauge32, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter64", "iso", "TimeTicks", "Integer32", "Unsigned32", "NotificationType", "IpAddress", "ModuleIdentity", "Bits", "Gauge32", "MibIdentifier", "Counter32")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
mgmtSecurity = ModuleIdentity((1, 3, 6, 1, 4, 1, 7244, 2, 11))
if mibBuilder.loadTexts: mgmtSecurity.setLastUpdated('201108310000Z')
if mibBuilder.loadTexts: mgmtSecurity.setOrganization('Quanta Computer Inc.')
if mibBuilder.loadTexts: mgmtSecurity.setContactInfo(' Customer Support Postal: Quanta Computer Inc. 4, Wen Ming 1 St., Kuei Shan Hsiang, Tao Yuan Shien, Taiwan, R.O.C. Tel: +886 3 328 0050 E-Mail: support@quantatw.com')
if mibBuilder.loadTexts: mgmtSecurity.setDescription('The Private MIB for Security')
agentSSLConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 7244, 2, 11, 1))
agentSSLAdminMode = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 11, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSSLAdminMode.setStatus('current')
if mibBuilder.loadTexts: agentSSLAdminMode.setDescription('Configures whether the SSL service is enabled on this switch. The default value is disable(2).')
agentSSLSecurePort = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 11, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSSLSecurePort.setStatus('current')
if mibBuilder.loadTexts: agentSSLSecurePort.setDescription('Configures the port the SSL service will respond on. The default value is 443.')
agentSSLProtocolLevel = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 11, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ssl30", 1), ("tls10", 2), ("both", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSSLProtocolLevel.setStatus('current')
if mibBuilder.loadTexts: agentSSLProtocolLevel.setDescription('Configures which protocol versions of SSL are enabled on this switch. The default value is both(3).')
agentSSLMaxSessions = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 11, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSSLMaxSessions.setStatus('current')
if mibBuilder.loadTexts: agentSSLMaxSessions.setDescription('Configures the maximum number of allowable SSL sessions. The default value is 16.')
agentSSLHardTimeout = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 11, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 168))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSSLHardTimeout.setStatus('current')
if mibBuilder.loadTexts: agentSSLHardTimeout.setDescription('Configures the hard timeout for SSL sessions in hours. The default value is 24 hours.')
agentSSLSoftTimeout = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 11, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSSLSoftTimeout.setStatus('current')
if mibBuilder.loadTexts: agentSSLSoftTimeout.setDescription('Configures the soft (activity) timeout for SSL sessions in minutes. The default value is 5 minutes.')
agentSSLCertificatePresent = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 11, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSSLCertificatePresent.setStatus('current')
if mibBuilder.loadTexts: agentSSLCertificatePresent.setDescription('Boolean value indicating whether SSL certificate files exist on the device.')
agentSSLCertificateControl = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 11, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noop", 1), ("generate", 2), ("delete", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSSLCertificateControl.setStatus('current')
if mibBuilder.loadTexts: agentSSLCertificateControl.setDescription('Controls certificate generation and deletion. Always returns noop(1).')
agentSSLCertificateGenerationStatus = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 11, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSSLCertificateGenerationStatus.setStatus('current')
if mibBuilder.loadTexts: agentSSLCertificateGenerationStatus.setDescription('Indicates whether certificate files are currently being generated.')
agentSSHConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 7244, 2, 11, 2))
agentSSHAdminMode = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 11, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSSHAdminMode.setStatus('current')
if mibBuilder.loadTexts: agentSSHAdminMode.setDescription('Configures whether the SSH service is enabled on this switch. The default value is disable(2).')
agentSSHProtocolLevel = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 11, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ssh10", 1), ("ssh20", 2), ("both", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSSHProtocolLevel.setStatus('current')
if mibBuilder.loadTexts: agentSSHProtocolLevel.setDescription('Configures which protocol versions of SSH are enabled on this switch. The default value is both(3).')
agentSSHSessionsCount = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 11, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSSHSessionsCount.setStatus('current')
if mibBuilder.loadTexts: agentSSHSessionsCount.setDescription('Current number of active SSH sessions on this switch.')
agentSSHMaxSessionsCount = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 11, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 5))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSSHMaxSessionsCount.setStatus('current')
if mibBuilder.loadTexts: agentSSHMaxSessionsCount.setDescription('Max number of SSH sessions permitted on this switch.')
agentSSHSessionTimeout = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 11, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 160))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSSHSessionTimeout.setStatus('current')
if mibBuilder.loadTexts: agentSSHSessionTimeout.setDescription('ssh idle timeout value for this switch im minutes.')
agentSSHKeysPresent = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 11, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("dsa", 1), ("rsa", 2), ("both", 3), ("none", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSSHKeysPresent.setStatus('current')
if mibBuilder.loadTexts: agentSSHKeysPresent.setDescription('Indicates what key files are present on the device, if any.')
agentSSHKeyGenerationStatus = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 11, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("dsa", 1), ("rsa", 2), ("both", 3), ("none", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSSHKeyGenerationStatus.setStatus('current')
if mibBuilder.loadTexts: agentSSHKeyGenerationStatus.setDescription('Indicates what key files are currently being generated, if any.')
agentSSHRSAKeyControl = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 11, 2, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noop", 1), ("generate", 2), ("delete", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSSHRSAKeyControl.setStatus('current')
if mibBuilder.loadTexts: agentSSHRSAKeyControl.setDescription('Controls RSA key generation and deletion. Always returns noop(1).')
agentSSHDSAKeyControl = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 11, 2, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noop", 1), ("generate", 2), ("delete", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSSHDSAKeyControl.setStatus('current')
if mibBuilder.loadTexts: agentSSHDSAKeyControl.setDescription('Controls DSA key generation and deletion. Always returns noop(1).')
mibBuilder.exportSymbols("MGMT-SECURITY-MIB", agentSSHSessionsCount=agentSSHSessionsCount, PYSNMP_MODULE_ID=mgmtSecurity, agentSSLMaxSessions=agentSSLMaxSessions, agentSSHKeyGenerationStatus=agentSSHKeyGenerationStatus, agentSSHSessionTimeout=agentSSHSessionTimeout, agentSSLCertificateControl=agentSSLCertificateControl, mgmtSecurity=mgmtSecurity, agentSSLProtocolLevel=agentSSLProtocolLevel, agentSSLCertificateGenerationStatus=agentSSLCertificateGenerationStatus, agentSSLConfigGroup=agentSSLConfigGroup, agentSSHAdminMode=agentSSHAdminMode, agentSSHRSAKeyControl=agentSSHRSAKeyControl, agentSSHKeysPresent=agentSSHKeysPresent, agentSSHConfigGroup=agentSSHConfigGroup, agentSSHMaxSessionsCount=agentSSHMaxSessionsCount, agentSSLAdminMode=agentSSLAdminMode, agentSSLSoftTimeout=agentSSLSoftTimeout, agentSSLHardTimeout=agentSSLHardTimeout, agentSSHDSAKeyControl=agentSSHDSAKeyControl, agentSSHProtocolLevel=agentSSHProtocolLevel, agentSSLSecurePort=agentSSLSecurePort, agentSSLCertificatePresent=agentSSLCertificatePresent)
