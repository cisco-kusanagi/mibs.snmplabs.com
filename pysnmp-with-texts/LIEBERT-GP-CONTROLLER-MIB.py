#
# PySNMP MIB module LIEBERT-GP-CONTROLLER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LIEBERT-GP-CONTROLLER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:06:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
lgpController, liebertControllerModuleReg = mibBuilder.importSymbols("LIEBERT-GP-REGISTRATION-MIB", "lgpController", "liebertControllerModuleReg")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Unsigned32, ObjectIdentity, Bits, ModuleIdentity, Counter64, Integer32, NotificationType, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Unsigned32", "ObjectIdentity", "Bits", "ModuleIdentity", "Counter64", "Integer32", "NotificationType", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
liebertControllerModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 7, 1))
liebertControllerModule.setRevisions(('2008-07-02 00:00', '2008-01-10 00:00', '2006-02-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: liebertControllerModule.setRevisionsDescriptions(('Removed unnecessary item from import statement', 'Modified contact email address.', 'Added support for Liebert DS Unit.',))
if mibBuilder.loadTexts: liebertControllerModule.setLastUpdated('200807020000Z')
if mibBuilder.loadTexts: liebertControllerModule.setOrganization('Liebert Corporation')
if mibBuilder.loadTexts: liebertControllerModule.setContactInfo('Contact: Technical Support Postal: Liebert Corporation 1050 Dearborn Drive P.O. Box 29186 Columbus OH, 43229 US Tel: +1 (800) 222-5877 E-mail: liebert.monitoring@emerson.com Web: www.liebert.com Author: Gregory M. Hoge')
if mibBuilder.loadTexts: liebertControllerModule.setDescription("The MIB module used to specify Liebert Controller OIDs Copyright 2000-2008 Liebert Corporation. All rights reserved. Reproduction of this document is authorized on the condition that the forgoing copyright notice is included. This Specification is supplied 'AS IS' and Liebert Corporation makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
lgpCtrlNumberInstalledControlModules = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 6, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpCtrlNumberInstalledControlModules.setStatus('current')
if mibBuilder.loadTexts: lgpCtrlNumberInstalledControlModules.setDescription('The number of control modules installed in the device.')
lgpCtrlNumberFailedControlModules = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 6, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpCtrlNumberFailedControlModules.setStatus('current')
if mibBuilder.loadTexts: lgpCtrlNumberFailedControlModules.setDescription('The number of control modules in the device that have failed.')
lgpCtrlNumberRedundantControlModules = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 6, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpCtrlNumberRedundantControlModules.setStatus('current')
if mibBuilder.loadTexts: lgpCtrlNumberRedundantControlModules.setDescription('The number of redundant control modules installed in the device.')
lgpCtrlNumberControlModuleWarnings = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 6, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpCtrlNumberControlModuleWarnings.setStatus('current')
if mibBuilder.loadTexts: lgpCtrlNumberControlModuleWarnings.setDescription('The number of control modules in the device that have a warning.')
lgpCtrlBoardBatteryVoltage = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 6, 6), Unsigned32()).setUnits('.01 Volts').setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpCtrlBoardBatteryVoltage.setStatus('current')
if mibBuilder.loadTexts: lgpCtrlBoardBatteryVoltage.setDescription('The control board battery voltage. Typically this battery is used to provide backup power to memory and other vital circuits.')
mibBuilder.exportSymbols("LIEBERT-GP-CONTROLLER-MIB", lgpCtrlBoardBatteryVoltage=lgpCtrlBoardBatteryVoltage, lgpCtrlNumberControlModuleWarnings=lgpCtrlNumberControlModuleWarnings, lgpCtrlNumberFailedControlModules=lgpCtrlNumberFailedControlModules, liebertControllerModule=liebertControllerModule, PYSNMP_MODULE_ID=liebertControllerModule, lgpCtrlNumberInstalledControlModules=lgpCtrlNumberInstalledControlModules, lgpCtrlNumberRedundantControlModules=lgpCtrlNumberRedundantControlModules)
