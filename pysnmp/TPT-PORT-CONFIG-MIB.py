#
# PySNMP MIB module TPT-PORT-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPT-PORT-CONFIG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:18:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, NotificationType, MibIdentifier, ModuleIdentity, Unsigned32, Bits, Counter64, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, Counter32, ObjectIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "MibIdentifier", "ModuleIdentity", "Unsigned32", "Bits", "Counter64", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "Counter32", "ObjectIdentity", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tpt_tpa_objs, = mibBuilder.importSymbols("TPT-TPAMIBS-MIB", "tpt-tpa-objs")
tpt_port_config_objs = ModuleIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4)).setLabel("tpt-port-config-objs")
tpt_port_config_objs.setRevisions(('2016-05-25 18:54',))
if mibBuilder.loadTexts: tpt_port_config_objs.setLastUpdated('201605251854Z')
if mibBuilder.loadTexts: tpt_port_config_objs.setOrganization('Trend Micro, Inc.')
class LineSpeed(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("default", 0), ("gigabit", 1), ("hundred-megabit", 2), ("ten-megabit", 3), ("ten-gigabit", 4), ("fourty-gigabit", 5))

class DuplexSetting(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("default", 0), ("half", 1), ("full", 2))

class AutoNegotiation(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("default", 0), ("on", 1), ("off", 2))

class EnabledOrNot(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class FailoverAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("block", 0), ("permit", 1))

class LinkDownMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("hub", 0), ("breaker", 1), ("wire", 2))

portConfigTable = MibTable((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1), )
if mibBuilder.loadTexts: portConfigTable.setStatus('current')
portConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1), ).setIndexNames((0, "TPT-PORT-CONFIG-MIB", "portConfigSlot"), (0, "TPT-PORT-CONFIG-MIB", "portConfigPort"))
if mibBuilder.loadTexts: portConfigEntry.setStatus('current')
portConfigSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portConfigSlot.setStatus('current')
portConfigPort = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portConfigPort.setStatus('current')
portConfigLineSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 3), LineSpeed()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portConfigLineSpeed.setStatus('current')
portConfigDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 4), DuplexSetting()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portConfigDuplex.setStatus('current')
portConfigAutoNeg = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 5), AutoNegotiation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portConfigAutoNeg.setStatus('current')
portConfigShutdown = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 6), EnabledOrNot()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portConfigShutdown.setStatus('current')
portConfigLoopback = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 7), EnabledOrNot()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portConfigLoopback.setStatus('current')
portConfigFailover = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 8), FailoverAction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portConfigFailover.setStatus('current')
portConfigLDSMode = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 9), LinkDownMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portConfigLDSMode.setStatus('current')
portConfigLDSTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portConfigLDSTimeout.setStatus('current')
mibBuilder.exportSymbols("TPT-PORT-CONFIG-MIB", portConfigEntry=portConfigEntry, FailoverAction=FailoverAction, portConfigLDSMode=portConfigLDSMode, tpt_port_config_objs=tpt_port_config_objs, portConfigDuplex=portConfigDuplex, portConfigLDSTimeout=portConfigLDSTimeout, LineSpeed=LineSpeed, AutoNegotiation=AutoNegotiation, portConfigAutoNeg=portConfigAutoNeg, DuplexSetting=DuplexSetting, portConfigTable=portConfigTable, portConfigLineSpeed=portConfigLineSpeed, PYSNMP_MODULE_ID=tpt_port_config_objs, LinkDownMode=LinkDownMode, portConfigShutdown=portConfigShutdown, EnabledOrNot=EnabledOrNot, portConfigSlot=portConfigSlot, portConfigLoopback=portConfigLoopback, portConfigFailover=portConfigFailover, portConfigPort=portConfigPort)
