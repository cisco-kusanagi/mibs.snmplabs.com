#
# PySNMP MIB module TRIPPLITE (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TRIPPLITE
# Produced by pysmi-0.3.4 at Wed May  1 15:27:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, ModuleIdentity, Unsigned32, Integer32, MibIdentifier, TimeTicks, Gauge32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Bits, IpAddress, Counter64, enterprises, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "Unsigned32", "Integer32", "MibIdentifier", "TimeTicks", "Gauge32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Bits", "IpAddress", "Counter64", "enterprises", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tripplite = ModuleIdentity((1, 3, 6, 1, 4, 1, 850))
tripplite.setRevisions(('2016-06-22 11:15',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tripplite.setRevisionsDescriptions(('Restructured Tripp Lite MIB files',))
if mibBuilder.loadTexts: tripplite.setLastUpdated('201606221115Z')
if mibBuilder.loadTexts: tripplite.setOrganization('Tripp Lite')
if mibBuilder.loadTexts: tripplite.setContactInfo('Software Engineering Tripp Lite 1111 W. 35th St. Chicago, IL 60609')
if mibBuilder.loadTexts: tripplite.setDescription("The base MIB module that defines the root objects from Tripp Lite's OID tree (850).")
mibBuilder.exportSymbols("TRIPPLITE", tripplite=tripplite, PYSNMP_MODULE_ID=tripplite)
