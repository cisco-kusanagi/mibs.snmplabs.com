#
# PySNMP MIB module ELTEX-MES-TRAPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-MES-TRAPS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:02:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
eltMes, = mibBuilder.importSymbols("ELTEX-MES", "eltMes")
rldot1dStpTrapVrblVID, rldot1dStpTrapVrblifIndex = mibBuilder.importSymbols("RADLAN-BRIDGEMIBOBJECTS-MIB", "rldot1dStpTrapVrblVID", "rldot1dStpTrapVrblifIndex")
rndErrorDesc, rndErrorSeverity = mibBuilder.importSymbols("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc", "rndErrorSeverity")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, TimeTicks, Integer32, MibIdentifier, Counter64, iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, Unsigned32, Counter32, Bits, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "Integer32", "MibIdentifier", "Counter64", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "Unsigned32", "Counter32", "Bits", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
eltMesNotifications = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 23, 0))
eltMesNotifications.setRevisions(('2012-07-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: eltMesNotifications.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: eltMesNotifications.setLastUpdated('201207130000Z')
if mibBuilder.loadTexts: eltMesNotifications.setOrganization('Eltex Enterprise Co, Ltd.')
if mibBuilder.loadTexts: eltMesNotifications.setContactInfo('www.eltex.nsk.ru')
if mibBuilder.loadTexts: eltMesNotifications.setDescription("This private MIB module defines Eltex's private notifications")
i2cBusFailure = NotificationType((1, 3, 6, 1, 4, 1, 35265, 1, 23, 0, 3)).setObjects(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"), ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: i2cBusFailure.setStatus('current')
if mibBuilder.loadTexts: i2cBusFailure.setDescription('An I2C bus malfunction detected. It means that a lot of I2C bus I/O transactions was completed unsuccessfully before and repairing efforts were vain. It is a critical event, all I2C-controllable HW nodes are unaccessible now.')
i2cBusOperational = NotificationType((1, 3, 6, 1, 4, 1, 35265, 1, 23, 0, 4)).setObjects(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"), ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: i2cBusOperational.setStatus('current')
if mibBuilder.loadTexts: i2cBusOperational.setDescription('An I2C bus is now operational. Appearance of this trap means that bus operation was stick before and is repaired now.')
transThresholdWarning = NotificationType((1, 3, 6, 1, 4, 1, 35265, 1, 23, 0, 5)).setObjects(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"), ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: transThresholdWarning.setStatus('current')
if mibBuilder.loadTexts: transThresholdWarning.setDescription('Particular value of temperature, voltage, current, output power or input power is outside of normal limits. Alarm indicates conditions associated with an in-operational link. Warning indicates conditions outside normally guaranteed bounds, but not necessary causes link failures')
transThresholdOK = NotificationType((1, 3, 6, 1, 4, 1, 35265, 1, 23, 0, 6)).setObjects(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"), ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: transThresholdOK.setStatus('current')
if mibBuilder.loadTexts: transThresholdOK.setDescription('Particular value of temperature, voltage, current, output power or input power is inside of normal limits.')
mibBuilder.exportSymbols("ELTEX-MES-TRAPS-MIB", transThresholdWarning=transThresholdWarning, i2cBusOperational=i2cBusOperational, transThresholdOK=transThresholdOK, PYSNMP_MODULE_ID=eltMesNotifications, i2cBusFailure=i2cBusFailure, eltMesNotifications=eltMesNotifications)
