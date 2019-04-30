#
# PySNMP MIB module ELTEX-MES-ENDOFMIB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-MES-ENDOFMIB-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:46:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
eltMes, = mibBuilder.importSymbols("ELTEX-MES", "eltMes")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Integer32, MibIdentifier, TimeTicks, Unsigned32, NotificationType, ModuleIdentity, IpAddress, Counter32, Bits, iso, ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Integer32", "MibIdentifier", "TimeTicks", "Unsigned32", "NotificationType", "ModuleIdentity", "IpAddress", "Counter32", "Bits", "iso", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
eltMesEndOfMibGroup = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1000))
eltMesEndOfMibGroup.setRevisions(('2012-07-13 00:00',))
if mibBuilder.loadTexts: eltMesEndOfMibGroup.setLastUpdated('201207130000Z')
if mibBuilder.loadTexts: eltMesEndOfMibGroup.setOrganization('Eltex Enterprise Co, Ltd.')
eltEndOfMib = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1000, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltEndOfMib.setStatus('current')
mibBuilder.exportSymbols("ELTEX-MES-ENDOFMIB-MIB", PYSNMP_MODULE_ID=eltMesEndOfMibGroup, eltMesEndOfMibGroup=eltMesEndOfMibGroup, eltEndOfMib=eltEndOfMib)
