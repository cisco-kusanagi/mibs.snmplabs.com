#
# PySNMP MIB module ELTEX-ENDOFMIB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-ENDOFMIB-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:00:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
elt, = mibBuilder.importSymbols("ELTEX-MIB", "elt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, TimeTicks, ModuleIdentity, Bits, Unsigned32, Gauge32, MibIdentifier, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, IpAddress, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "ModuleIdentity", "Bits", "Unsigned32", "Gauge32", "MibIdentifier", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "IpAddress", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
eltEndOfMibGroup = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1000))
eltEndOfMibGroup.setRevisions(('2012-07-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: eltEndOfMibGroup.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: eltEndOfMibGroup.setLastUpdated('201207130000Z')
if mibBuilder.loadTexts: eltEndOfMibGroup.setOrganization('Eltex Enterprise Co, Ltd.')
if mibBuilder.loadTexts: eltEndOfMibGroup.setContactInfo('www.eltex.nsk.ru')
if mibBuilder.loadTexts: eltEndOfMibGroup.setDescription('This private MIB module defines End of Eltex private MIBs.')
eltEndOfMib = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1000, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltEndOfMib.setStatus('current')
if mibBuilder.loadTexts: eltEndOfMib.setDescription(' This variable indicates this is the end of Eltex MIB.')
mibBuilder.exportSymbols("ELTEX-ENDOFMIB-MIB", eltEndOfMib=eltEndOfMib, eltEndOfMibGroup=eltEndOfMibGroup, PYSNMP_MODULE_ID=eltEndOfMibGroup)
