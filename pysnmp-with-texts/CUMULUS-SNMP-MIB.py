#
# PySNMP MIB module CUMULUS-SNMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CUMULUS-SNMP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:31:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, IpAddress, Counter64, enterprises, ModuleIdentity, Unsigned32, Bits, Counter32, ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, iso, MibIdentifier, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "Counter64", "enterprises", "ModuleIdentity", "Unsigned32", "Bits", "Counter32", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "iso", "MibIdentifier", "TimeTicks")
TextualConvention, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "DisplayString")
cumulusMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 40310))
cumulusMib.setRevisions(('2012-07-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cumulusMib.setRevisionsDescriptions(('Second version with new Enterprise number and discard counters',))
if mibBuilder.loadTexts: cumulusMib.setLastUpdated('201207230000Z')
if mibBuilder.loadTexts: cumulusMib.setOrganization('www.cumulusnetworks.com')
if mibBuilder.loadTexts: cumulusMib.setContactInfo('postal: Dinesh Dutt 650 Castro Street, suite 120-245 Mountain View, CA 94041 email: ddutt@cumulusnetworks.com')
if mibBuilder.loadTexts: cumulusMib.setDescription('Top-level infrastructure of the Cumulus enterprise MIB tree')
mibBuilder.exportSymbols("CUMULUS-SNMP-MIB", cumulusMib=cumulusMib, PYSNMP_MODULE_ID=cumulusMib)
