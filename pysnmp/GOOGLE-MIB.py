#
# PySNMP MIB module GOOGLE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GOOGLE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:06:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Integer32, TimeTicks, Counter32, Unsigned32, Bits, ModuleIdentity, Counter64, enterprises, IpAddress, Gauge32, MibIdentifier, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Integer32", "TimeTicks", "Counter32", "Unsigned32", "Bits", "ModuleIdentity", "Counter64", "enterprises", "IpAddress", "Gauge32", "MibIdentifier", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
google = ModuleIdentity((1, 3, 6, 1, 4, 1, 11129))
if mibBuilder.loadTexts: google.setLastUpdated('200407161000Z')
if mibBuilder.loadTexts: google.setOrganization('Google Inc.')
gsa = MibIdentifier((1, 3, 6, 1, 4, 1, 11129, 1))
mibBuilder.exportSymbols("GOOGLE-MIB", gsa=gsa, google=google, PYSNMP_MODULE_ID=google)
