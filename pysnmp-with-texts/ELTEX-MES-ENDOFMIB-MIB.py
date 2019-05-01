#
# PySNMP MIB module ELTEX-MES-ENDOFMIB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-MES-ENDOFMIB-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:01:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
eltMes, = mibBuilder.importSymbols("ELTEX-MES", "eltMes")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, TimeTicks, Counter64, ObjectIdentity, NotificationType, ModuleIdentity, IpAddress, Bits, Gauge32, Counter32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "TimeTicks", "Counter64", "ObjectIdentity", "NotificationType", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Counter32", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
eltMesEndOfMibGroup = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1000))
eltMesEndOfMibGroup.setRevisions(('2012-07-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: eltMesEndOfMibGroup.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: eltMesEndOfMibGroup.setLastUpdated('201207130000Z')
if mibBuilder.loadTexts: eltMesEndOfMibGroup.setOrganization('Eltex Enterprise Co, Ltd.')
if mibBuilder.loadTexts: eltMesEndOfMibGroup.setContactInfo('www.eltex.nsk.ru')
if mibBuilder.loadTexts: eltMesEndOfMibGroup.setDescription('This private MIB module defines End of Eltex private MIBs.')
eltEndOfMib = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1000, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltEndOfMib.setStatus('current')
if mibBuilder.loadTexts: eltEndOfMib.setDescription(' This variable indicates this is the end of Eltex MIB.')
mibBuilder.exportSymbols("ELTEX-MES-ENDOFMIB-MIB", PYSNMP_MODULE_ID=eltMesEndOfMibGroup, eltEndOfMib=eltEndOfMib, eltMesEndOfMibGroup=eltMesEndOfMibGroup)
