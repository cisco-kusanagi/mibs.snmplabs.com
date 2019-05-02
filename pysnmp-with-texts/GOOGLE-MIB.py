#
# PySNMP MIB module GOOGLE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GOOGLE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:19:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Unsigned32, Integer32, Gauge32, MibIdentifier, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress, enterprises, ObjectIdentity, Bits, TimeTicks, NotificationType, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Unsigned32", "Integer32", "Gauge32", "MibIdentifier", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress", "enterprises", "ObjectIdentity", "Bits", "TimeTicks", "NotificationType", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
google = ModuleIdentity((1, 3, 6, 1, 4, 1, 11129))
if mibBuilder.loadTexts: google.setLastUpdated('200407161000Z')
if mibBuilder.loadTexts: google.setOrganization('Google Inc.')
if mibBuilder.loadTexts: google.setContactInfo("This MIB is the root for all Enterprise specific SNMP variables exposed by Google's products postal: Ian Macdonald 1600 Amphitheatre Pkwy Mountain View, CA 94035 email: enterprise-support@google.com ")
if mibBuilder.loadTexts: google.setDescription("Initial Version for Google's root MIB")
gsa = MibIdentifier((1, 3, 6, 1, 4, 1, 11129, 1))
mibBuilder.exportSymbols("GOOGLE-MIB", PYSNMP_MODULE_ID=google, gsa=gsa, google=google)
