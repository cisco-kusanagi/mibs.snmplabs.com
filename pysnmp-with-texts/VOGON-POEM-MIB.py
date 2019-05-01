#
# PySNMP MIB module VOGON-POEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/VOGON-POEM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:35:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
snmpTraps, = mibBuilder.importSymbols("SNMPv2-MIB", "snmpTraps")
ObjectIdentity, ModuleIdentity, mib_2, Counter64, MibIdentifier, Unsigned32, IpAddress, NotificationType, Counter32, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "ModuleIdentity", "mib-2", "Counter64", "MibIdentifier", "Unsigned32", "IpAddress", "NotificationType", "Counter32", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
vogonpoem = ModuleIdentity((1, 3, 6, 1, 2, 1, 42))
if mibBuilder.loadTexts: vogonpoem.setLastUpdated('200006140000Z')
if mibBuilder.loadTexts: vogonpoem.setOrganization('Vogon inc.')
if mibBuilder.loadTexts: vogonpoem.setContactInfo('Prostetnic Vogon Jeltze Galactic Hyperspace Planning Council')
if mibBuilder.loadTexts: vogonpoem.setDescription('')
vogon = MibIdentifier((1, 3, 6, 1, 2, 1, 424242))
poemNumber = MibScalar((1, 3, 6, 1, 2, 1, 424242, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: poemNumber.setStatus('current')
if mibBuilder.loadTexts: poemNumber.setDescription('The number of vogon poems in this e-book.')
mibBuilder.exportSymbols("VOGON-POEM-MIB", PYSNMP_MODULE_ID=vogonpoem, vogon=vogon, poemNumber=poemNumber, vogonpoem=vogonpoem)
