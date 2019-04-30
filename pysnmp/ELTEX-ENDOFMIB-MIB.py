#
# PySNMP MIB module ELTEX-ENDOFMIB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-ENDOFMIB-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:45:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
elt, = mibBuilder.importSymbols("ELTEX-MIB", "elt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, IpAddress, Counter32, Gauge32, ObjectIdentity, Counter64, iso, ModuleIdentity, TimeTicks, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "IpAddress", "Counter32", "Gauge32", "ObjectIdentity", "Counter64", "iso", "ModuleIdentity", "TimeTicks", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
eltEndOfMibGroup = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1000))
eltEndOfMibGroup.setRevisions(('2012-07-13 00:00',))
if mibBuilder.loadTexts: eltEndOfMibGroup.setLastUpdated('201207130000Z')
if mibBuilder.loadTexts: eltEndOfMibGroup.setOrganization('Eltex Enterprise Co, Ltd.')
eltEndOfMib = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1000, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltEndOfMib.setStatus('current')
mibBuilder.exportSymbols("ELTEX-ENDOFMIB-MIB", eltEndOfMib=eltEndOfMib, PYSNMP_MODULE_ID=eltEndOfMibGroup, eltEndOfMibGroup=eltEndOfMibGroup)
