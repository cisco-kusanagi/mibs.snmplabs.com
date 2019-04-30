#
# PySNMP MIB module CUMULUS-SNMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CUMULUS-SNMP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:16:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, IpAddress, Integer32, ModuleIdentity, Gauge32, Counter64, Unsigned32, enterprises, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks, ObjectIdentity, Counter32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "IpAddress", "Integer32", "ModuleIdentity", "Gauge32", "Counter64", "Unsigned32", "enterprises", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks", "ObjectIdentity", "Counter32", "NotificationType")
TextualConvention, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "DisplayString")
cumulusMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 40310))
cumulusMib.setRevisions(('2012-07-23 00:00',))
if mibBuilder.loadTexts: cumulusMib.setLastUpdated('201207230000Z')
if mibBuilder.loadTexts: cumulusMib.setOrganization('www.cumulusnetworks.com')
mibBuilder.exportSymbols("CUMULUS-SNMP-MIB", PYSNMP_MODULE_ID=cumulusMib, cumulusMib=cumulusMib)
