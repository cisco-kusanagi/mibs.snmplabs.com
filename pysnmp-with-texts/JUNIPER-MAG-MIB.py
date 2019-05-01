#
# PySNMP MIB module JUNIPER-MAG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-MAG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:00:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
jnxMagMibRoot, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMagMibRoot")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Integer32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, Gauge32, ObjectIdentity, Counter32, Unsigned32, Counter64, MibIdentifier, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Integer32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "Gauge32", "ObjectIdentity", "Counter32", "Unsigned32", "Counter64", "MibIdentifier", "Bits", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
jnxMagMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 65, 1))
jnxMagMib.setRevisions(('2010-02-20 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: jnxMagMib.setRevisionsDescriptions(('Creation Date',))
if mibBuilder.loadTexts: jnxMagMib.setLastUpdated('201002201210Z')
if mibBuilder.loadTexts: jnxMagMib.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: jnxMagMib.setContactInfo('Juniper Technical Assistance Center Juniper Networks, Inc. 1194 N. Mathilda Avenue Sunnyvale, CA 94089 E-mail: support@juniper.net HTTP://www.juniper.net')
if mibBuilder.loadTexts: jnxMagMib.setDescription('These MIB objects pertain to Secure access, infranet controller and WAN acceleration service modules?')
jnxMagNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 65, 1, 0))
jnxMagObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 65, 1, 1))
jnxMagSSOObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 65, 1, 1, 1))
jnxMagSSOAuthTokenAttempt = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 65, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMagSSOAuthTokenAttempt.setStatus('current')
if mibBuilder.loadTexts: jnxMagSSOAuthTokenAttempt.setDescription('Number of Auth Token attempts made')
jnxMagSSOFailedAuthToken = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 65, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMagSSOFailedAuthToken.setStatus('current')
if mibBuilder.loadTexts: jnxMagSSOFailedAuthToken.setDescription('Number of Failed Auth Token ')
jnxMagSSOValidationError = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 65, 1, 0, 1))
if mibBuilder.loadTexts: jnxMagSSOValidationError.setStatus('current')
if mibBuilder.loadTexts: jnxMagSSOValidationError.setDescription(' Auth Token Validation error')
mibBuilder.exportSymbols("JUNIPER-MAG-MIB", jnxMagSSOObjects=jnxMagSSOObjects, jnxMagNotifications=jnxMagNotifications, jnxMagObjects=jnxMagObjects, jnxMagSSOAuthTokenAttempt=jnxMagSSOAuthTokenAttempt, jnxMagMib=jnxMagMib, PYSNMP_MODULE_ID=jnxMagMib, jnxMagSSOValidationError=jnxMagSSOValidationError, jnxMagSSOFailedAuthToken=jnxMagSSOFailedAuthToken)
