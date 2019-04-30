#
# PySNMP MIB module TPT-TANK-NOTIFY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPT-TANK-NOTIFY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:19:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Unsigned32, Counter64, iso, Bits, Counter32, ModuleIdentity, MibIdentifier, ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Unsigned32", "Counter64", "iso", "Bits", "Counter32", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tptMiscNotifyDeviceID, = mibBuilder.importSymbols("TPT-MISC-NOTIFY-MIB", "tptMiscNotifyDeviceID")
tpt_tpa_eventsV2, tpt_tpa_objs, tpt_tpa_unkparams = mibBuilder.importSymbols("TPT-TPAMIBS-MIB", "tpt-tpa-eventsV2", "tpt-tpa-objs", "tpt-tpa-unkparams")
tpt_tank_notify = ModuleIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 11)).setLabel("tpt-tank-notify")
tpt_tank_notify.setRevisions(('2016-05-25 18:54',))
if mibBuilder.loadTexts: tpt_tank_notify.setLastUpdated('201605251854Z')
if mibBuilder.loadTexts: tpt_tank_notify.setOrganization('Trend Micro, Inc.')
class ExternalVIStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class WebFilterStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("uninitialized", 1), ("success", 2), ("timeout", 3), ("failure", 4))

tptTankNotifyExternalVIStatus = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 151), ExternalVIStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptTankNotifyExternalVIStatus.setStatus('current')
tptTankNotifyWebFilterStatus = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 152), WebFilterStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptTankNotifyWebFilterStatus.setStatus('current')
tptTankNotifyExternalVI = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 22)).setObjects(("TPT-MISC-NOTIFY-MIB", "tptMiscNotifyDeviceID"), ("TPT-TANK-NOTIFY-MIB", "tptTankNotifyExternalVIStatus"))
if mibBuilder.loadTexts: tptTankNotifyExternalVI.setStatus('current')
tptTankNotifyWebFilter = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 23)).setObjects(("TPT-MISC-NOTIFY-MIB", "tptMiscNotifyDeviceID"), ("TPT-TANK-NOTIFY-MIB", "tptTankNotifyWebFilterStatus"))
if mibBuilder.loadTexts: tptTankNotifyWebFilter.setStatus('current')
mibBuilder.exportSymbols("TPT-TANK-NOTIFY-MIB", ExternalVIStatus=ExternalVIStatus, tpt_tank_notify=tpt_tank_notify, tptTankNotifyExternalVI=tptTankNotifyExternalVI, WebFilterStatus=WebFilterStatus, tptTankNotifyExternalVIStatus=tptTankNotifyExternalVIStatus, tptTankNotifyWebFilter=tptTankNotifyWebFilter, tptTankNotifyWebFilterStatus=tptTankNotifyWebFilterStatus, PYSNMP_MODULE_ID=tpt_tank_notify)
