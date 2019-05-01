#
# PySNMP MIB module RADLAN-DEBUGCAPABILITIES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-DEBUGCAPABILITIES-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:45:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Integer32, ModuleIdentity, Counter64, iso, ObjectIdentity, Bits, TimeTicks, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, Gauge32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Integer32", "ModuleIdentity", "Counter64", "iso", "ObjectIdentity", "Bits", "TimeTicks", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "Gauge32", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rlDebugCapabilities = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 206))
rlDebugCapabilities.setRevisions(('2011-01-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlDebugCapabilities.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rlDebugCapabilities.setLastUpdated('201101050000Z')
if mibBuilder.loadTexts: rlDebugCapabilities.setOrganization('Radlan - a MARVELL company. Marvell Semiconductor, Inc.')
if mibBuilder.loadTexts: rlDebugCapabilities.setContactInfo('www.marvell.com')
if mibBuilder.loadTexts: rlDebugCapabilities.setDescription('This private MIB module is used for achieving extended debugging capablities for the device. For example: greater management capabilies for technical support users.')
rlDebugCapabilitiesPassword = MibScalar((1, 3, 6, 1, 4, 1, 89, 206, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDebugCapabilitiesPassword.setStatus('current')
if mibBuilder.loadTexts: rlDebugCapabilitiesPassword.setDescription('A user intereseted to obtain extended debug capabilities should SET this MIB to a well known secret value (it is intended to be used only by authorized users). Most often, this value will be based on the device MAC address. Upon setting the correct value, the SET operation will return noError. Otherwise, wrongValue will return to the caller. GET operation on this MIB will reurn a value of length 0.')
mibBuilder.exportSymbols("RADLAN-DEBUGCAPABILITIES-MIB", PYSNMP_MODULE_ID=rlDebugCapabilities, rlDebugCapabilitiesPassword=rlDebugCapabilitiesPassword, rlDebugCapabilities=rlDebugCapabilities)
