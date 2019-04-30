#
# PySNMP MIB module VOGON-POEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/VOGON-POEM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:28:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
snmpTraps, = mibBuilder.importSymbols("SNMPv2-MIB", "snmpTraps")
Gauge32, mib_2, TimeTicks, iso, Bits, Integer32, IpAddress, Counter32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ModuleIdentity, Unsigned32, NotificationType, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "mib-2", "TimeTicks", "iso", "Bits", "Integer32", "IpAddress", "Counter32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ModuleIdentity", "Unsigned32", "NotificationType", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
vogonpoem = ModuleIdentity((1, 3, 6, 1, 2, 1, 42))
if mibBuilder.loadTexts: vogonpoem.setLastUpdated('200006140000Z')
if mibBuilder.loadTexts: vogonpoem.setOrganization('Vogon inc.')
vogon = MibIdentifier((1, 3, 6, 1, 2, 1, 424242))
poemNumber = MibScalar((1, 3, 6, 1, 2, 1, 424242, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: poemNumber.setStatus('current')
mibBuilder.exportSymbols("VOGON-POEM-MIB", PYSNMP_MODULE_ID=vogonpoem, poemNumber=poemNumber, vogonpoem=vogonpoem, vogon=vogon)
