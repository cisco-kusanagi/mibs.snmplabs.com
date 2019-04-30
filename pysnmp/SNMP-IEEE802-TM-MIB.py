#
# PySNMP MIB module SNMP-IEEE802-TM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SNMP-IEEE802-TM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:00:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Gauge32, ModuleIdentity, snmpDomains, Integer32, Counter32, ObjectIdentity, TimeTicks, Bits, Unsigned32, IpAddress, MibIdentifier, snmpModules, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "ModuleIdentity", "snmpDomains", "Integer32", "Counter32", "ObjectIdentity", "TimeTicks", "Bits", "Unsigned32", "IpAddress", "MibIdentifier", "snmpModules", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
snmpIeee802TmMib = ModuleIdentity((1, 3, 6, 1, 6, 3, 21))
snmpIeee802TmMib.setRevisions(('2006-11-21 00:00',))
if mibBuilder.loadTexts: snmpIeee802TmMib.setLastUpdated('200611210000Z')
if mibBuilder.loadTexts: snmpIeee802TmMib.setOrganization('IETF Operations and Management Area')
snmpIeee802Domain = ObjectIdentity((1, 3, 6, 1, 6, 1, 6))
if mibBuilder.loadTexts: snmpIeee802Domain.setStatus('current')
mibBuilder.exportSymbols("SNMP-IEEE802-TM-MIB", snmpIeee802TmMib=snmpIeee802TmMib, PYSNMP_MODULE_ID=snmpIeee802TmMib, snmpIeee802Domain=snmpIeee802Domain)
