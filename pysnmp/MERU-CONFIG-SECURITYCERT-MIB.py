#
# PySNMP MIB module MERU-CONFIG-SECURITYCERT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MERU-CONFIG-SECURITYCERT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:01:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
Ipv6Address, = mibBuilder.importSymbols("IPV6-TC", "Ipv6Address")
mwConfiguration, = mibBuilder.importSymbols("MERU-SMI", "mwConfiguration")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, TimeTicks, NotificationType, enterprises, Integer32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, iso, ObjectIdentity, Bits, IpAddress, ModuleIdentity, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "TimeTicks", "NotificationType", "enterprises", "Integer32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "iso", "ObjectIdentity", "Bits", "IpAddress", "ModuleIdentity", "Unsigned32", "Counter32")
TextualConvention, DateAndTime, DisplayString, MacAddress, TruthValue, RowStatus, TimeInterval, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "DisplayString", "MacAddress", "TruthValue", "RowStatus", "TimeInterval", "TimeStamp")
mwConfigSecurityCert = ModuleIdentity((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 10))
if mibBuilder.loadTexts: mwConfigSecurityCert.setLastUpdated('200506050000Z')
if mibBuilder.loadTexts: mwConfigSecurityCert.setOrganization('Meru Networks')
mwSslCertInput = MibIdentifier((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 10, 2))
mwSslCert = MibIdentifier((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 10, 3))
mwSslCertInputCertificateName = MibScalar((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 10, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwSslCertInputCertificateName.setStatus('current')
mwSslCertInputPfxPassword = MibScalar((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 10, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwSslCertInputPfxPassword.setStatus('current')
mwSslCertCertificateName = MibScalar((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 10, 3, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwSslCertCertificateName.setStatus('current')
mwSslCertCertFormattedText = MibScalar((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 10, 3, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwSslCertCertFormattedText.setStatus('current')
mibBuilder.exportSymbols("MERU-CONFIG-SECURITYCERT-MIB", mwSslCertInput=mwSslCertInput, mwSslCertInputPfxPassword=mwSslCertInputPfxPassword, mwConfigSecurityCert=mwConfigSecurityCert, PYSNMP_MODULE_ID=mwConfigSecurityCert, mwSslCertCertFormattedText=mwSslCertCertFormattedText, mwSslCertCertificateName=mwSslCertCertificateName, mwSslCertInputCertificateName=mwSslCertInputCertificateName, mwSslCert=mwSslCert)
