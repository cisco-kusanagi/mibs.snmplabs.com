#
# PySNMP MIB module JUNIPER-MAG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-MAG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:49:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
jnxMagMibRoot, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMagMibRoot")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, TimeTicks, Gauge32, Integer32, Bits, NotificationType, iso, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, ObjectIdentity, Counter32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "TimeTicks", "Gauge32", "Integer32", "Bits", "NotificationType", "iso", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "ObjectIdentity", "Counter32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
jnxMagMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 65, 1))
jnxMagMib.setRevisions(('2010-02-20 12:00',))
if mibBuilder.loadTexts: jnxMagMib.setLastUpdated('201002201210Z')
if mibBuilder.loadTexts: jnxMagMib.setOrganization('Juniper Networks, Inc.')
jnxMagNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 65, 1, 0))
jnxMagObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 65, 1, 1))
jnxMagSSOObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 65, 1, 1, 1))
jnxMagSSOAuthTokenAttempt = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 65, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMagSSOAuthTokenAttempt.setStatus('current')
jnxMagSSOFailedAuthToken = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 65, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMagSSOFailedAuthToken.setStatus('current')
jnxMagSSOValidationError = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 65, 1, 0, 1))
if mibBuilder.loadTexts: jnxMagSSOValidationError.setStatus('current')
mibBuilder.exportSymbols("JUNIPER-MAG-MIB", jnxMagNotifications=jnxMagNotifications, jnxMagMib=jnxMagMib, jnxMagSSOValidationError=jnxMagSSOValidationError, jnxMagObjects=jnxMagObjects, jnxMagSSOAuthTokenAttempt=jnxMagSSOAuthTokenAttempt, jnxMagSSOFailedAuthToken=jnxMagSSOFailedAuthToken, PYSNMP_MODULE_ID=jnxMagMib, jnxMagSSOObjects=jnxMagSSOObjects)
