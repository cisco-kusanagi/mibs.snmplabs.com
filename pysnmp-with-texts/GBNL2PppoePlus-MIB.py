#
# PySNMP MIB module GBNL2PppoePlus-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GBNL2PppoePlus-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:18:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
gbnL2, = mibBuilder.importSymbols("GREENTECH-MASTER-MIB", "gbnL2")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Bits, iso, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Integer32, Gauge32, TimeTicks, IpAddress, Unsigned32, MibIdentifier, Counter64, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Integer32", "Gauge32", "TimeTicks", "IpAddress", "Unsigned32", "MibIdentifier", "Counter64", "ObjectIdentity", "NotificationType")
RowStatus, TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "TruthValue", "DisplayString")
gbnL2PppoePlus = ModuleIdentity((1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 6))
gbnL2PppoePlus.setRevisions(('1907-11-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: gbnL2PppoePlus.setRevisionsDescriptions(('Initial MIB creation.',))
if mibBuilder.loadTexts: gbnL2PppoePlus.setLastUpdated('0711220000Z')
if mibBuilder.loadTexts: gbnL2PppoePlus.setOrganization('Greentech')
if mibBuilder.loadTexts: gbnL2PppoePlus.setContactInfo('Adam Armstrong E-mail: adama@observium.org')
if mibBuilder.loadTexts: gbnL2PppoePlus.setDescription('GBN Enterprise MIB definition.')
pppoeplusOnOff = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 6, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppoeplusOnOff.setStatus('current')
if mibBuilder.loadTexts: pppoeplusOnOff.setDescription('start/stop pppoe plus.Default is off')
pppoeplusType = MibScalar((1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 6, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("standard", 0), ("huawei", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppoeplusType.setStatus('current')
if mibBuilder.loadTexts: pppoeplusType.setDescription('ppoeplus type.')
mibBuilder.exportSymbols("GBNL2PppoePlus-MIB", gbnL2PppoePlus=gbnL2PppoePlus, pppoeplusOnOff=pppoeplusOnOff, PYSNMP_MODULE_ID=gbnL2PppoePlus, pppoeplusType=pppoeplusType)
