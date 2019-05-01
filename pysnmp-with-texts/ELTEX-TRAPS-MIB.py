#
# PySNMP MIB module ELTEX-TRAPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-TRAPS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:02:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
elt, = mibBuilder.importSymbols("ELTEX-MIB", "elt")
rldot1dStpTrapVrblVID, rldot1dStpTrapVrblifIndex = mibBuilder.importSymbols("RADLAN-BRIDGEMIBOBJECTS-MIB", "rldot1dStpTrapVrblVID", "rldot1dStpTrapVrblifIndex")
rndErrorSeverity, rndErrorDesc = mibBuilder.importSymbols("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity", "rndErrorDesc")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Counter64, Gauge32, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, IpAddress, Bits, Counter32, ModuleIdentity, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "Gauge32", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "IpAddress", "Bits", "Counter32", "ModuleIdentity", "TimeTicks", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
eltNotifications = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 0))
eltNotifications.setRevisions(('2012-07-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: eltNotifications.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: eltNotifications.setLastUpdated('201207130000Z')
if mibBuilder.loadTexts: eltNotifications.setOrganization('Eltex Enterprise Co, Ltd.')
if mibBuilder.loadTexts: eltNotifications.setContactInfo('www.eltex.nsk.ru')
if mibBuilder.loadTexts: eltNotifications.setDescription("This private MIB module defines Eltex's private notifications")
i2cBusFailure = NotificationType((1, 3, 6, 1, 4, 1, 35265, 0, 3)).setObjects(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"), ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: i2cBusFailure.setStatus('current')
if mibBuilder.loadTexts: i2cBusFailure.setDescription('An I2C bus malfunction detected. It means that a lot of I2C bus I/O transactions was completed unsuccessfully before and repairing efforts were vain. It is a critical event, all I2C-controllable HW nodes are unaccessible now.')
i2cBusOperational = NotificationType((1, 3, 6, 1, 4, 1, 35265, 0, 4)).setObjects(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"), ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: i2cBusOperational.setStatus('current')
if mibBuilder.loadTexts: i2cBusOperational.setDescription('An I2C bus is now operational. Appearance of this trap means that bus operation was stick before and is repaired now.')
mibBuilder.exportSymbols("ELTEX-TRAPS-MIB", i2cBusOperational=i2cBusOperational, PYSNMP_MODULE_ID=eltNotifications, eltNotifications=eltNotifications, i2cBusFailure=i2cBusFailure)
