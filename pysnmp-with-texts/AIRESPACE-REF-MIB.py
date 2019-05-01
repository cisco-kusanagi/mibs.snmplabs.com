#
# PySNMP MIB module AIRESPACE-REF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AIRESPACE-REF-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:16:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, TimeTicks, ObjectIdentity, Integer32, Gauge32, MibIdentifier, Counter64, Counter32, NotificationType, IpAddress, iso, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "ObjectIdentity", "Integer32", "Gauge32", "MibIdentifier", "Counter64", "Counter32", "NotificationType", "IpAddress", "iso", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
airespace = ModuleIdentity((1, 3, 6, 1, 4, 1, 14179))
airespace.setRevisions(('2005-12-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: airespace.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: airespace.setLastUpdated('200512190000Z')
if mibBuilder.loadTexts: airespace.setOrganization('Airespace, Inc.')
if mibBuilder.loadTexts: airespace.setContactInfo(' Cisco Systems, Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS Email: cs-wnbu-snmp@cisco.com')
if mibBuilder.loadTexts: airespace.setDescription('The Structure of Management Information for the Airespace enterprise.')
mibBuilder.exportSymbols("AIRESPACE-REF-MIB", airespace=airespace, PYSNMP_MODULE_ID=airespace)
