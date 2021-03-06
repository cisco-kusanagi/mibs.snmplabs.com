#
# PySNMP MIB module ALCATEL-IND1-TIMETRA-GLOBAL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALCATEL-IND1-TIMETRA-GLOBAL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:01:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Unsigned32, enterprises, Bits, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, MibIdentifier, IpAddress, iso, Integer32, TimeTicks, ObjectIdentity, NotificationType, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "enterprises", "Bits", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "MibIdentifier", "IpAddress", "iso", "Integer32", "TimeTicks", "ObjectIdentity", "NotificationType", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
timetraGlobalMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 6527, 1, 1, 1))
timetraGlobalMIBModule.setRevisions(('1908-01-01 00:00', '1907-01-01 00:00', '1905-08-31 00:00', '1905-01-24 00:00', '1904-01-15 00:00', '1903-01-20 00:00', '1900-08-14 00:00',))
if mibBuilder.loadTexts: timetraGlobalMIBModule.setLastUpdated('0801010000Z')
if mibBuilder.loadTexts: timetraGlobalMIBModule.setOrganization('Alcatel')
timetra = MibIdentifier((1, 3, 6, 1, 4, 1, 6527))
timetraReg = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 1))
timetraModules = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 1, 1))
timetraSRMIBModules = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 1, 1, 3))
timetraCapabilityModule = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 1, 1, 4))
timetra7750CapModule = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 1, 1, 4, 1))
timetra7450CapModule = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 1, 1, 4, 2))
timetra7710CapModule = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 1, 1, 4, 3))
alcatelCommonMIBModules = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 1, 1, 5))
timetraServiceRouters = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 1, 3))
tmnxModelSR1Reg = ObjectIdentity((1, 3, 6, 1, 4, 1, 6527, 1, 3, 1))
if mibBuilder.loadTexts: tmnxModelSR1Reg.setStatus('current')
tmnxModelSR4Reg = ObjectIdentity((1, 3, 6, 1, 4, 1, 6527, 1, 3, 2))
if mibBuilder.loadTexts: tmnxModelSR4Reg.setStatus('current')
tmnxModelSR12Reg = ObjectIdentity((1, 3, 6, 1, 4, 1, 6527, 1, 3, 3))
if mibBuilder.loadTexts: tmnxModelSR12Reg.setStatus('current')
tmnxModelSR7Reg = ObjectIdentity((1, 3, 6, 1, 4, 1, 6527, 1, 3, 4))
if mibBuilder.loadTexts: tmnxModelSR7Reg.setStatus('current')
tmnxModelSR6Reg = ObjectIdentity((1, 3, 6, 1, 4, 1, 6527, 1, 3, 5))
if mibBuilder.loadTexts: tmnxModelSR6Reg.setStatus('current')
timetraServiceSwitches = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 1, 6))
tmnxModelESS1Reg = ObjectIdentity((1, 3, 6, 1, 4, 1, 6527, 1, 6, 1))
if mibBuilder.loadTexts: tmnxModelESS1Reg.setStatus('current')
tmnxModelESS4Reg = ObjectIdentity((1, 3, 6, 1, 4, 1, 6527, 1, 6, 2))
if mibBuilder.loadTexts: tmnxModelESS4Reg.setStatus('current')
tmnxModelESS7Reg = ObjectIdentity((1, 3, 6, 1, 4, 1, 6527, 1, 6, 3))
if mibBuilder.loadTexts: tmnxModelESS7Reg.setStatus('current')
tmnxModelESS12Reg = ObjectIdentity((1, 3, 6, 1, 4, 1, 6527, 1, 6, 4))
if mibBuilder.loadTexts: tmnxModelESS12Reg.setStatus('current')
tmnxModelESS6Reg = ObjectIdentity((1, 3, 6, 1, 4, 1, 6527, 1, 6, 5))
if mibBuilder.loadTexts: tmnxModelESS6Reg.setStatus('current')
tmnxModelESS6vReg = ObjectIdentity((1, 3, 6, 1, 4, 1, 6527, 1, 6, 6))
if mibBuilder.loadTexts: tmnxModelESS6vReg.setStatus('current')
alcatel7710ServiceRouters = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 1, 9))
tmnxModel7710SRc12Reg = ObjectIdentity((1, 3, 6, 1, 4, 1, 6527, 1, 9, 1))
if mibBuilder.loadTexts: tmnxModel7710SRc12Reg.setStatus('current')
tmnxModel7710SRc4Reg = ObjectIdentity((1, 3, 6, 1, 4, 1, 6527, 1, 9, 2))
if mibBuilder.loadTexts: tmnxModel7710SRc4Reg.setStatus('current')
timetraGeneric = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 2))
timetraProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3))
tmnxSRMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1))
tmnxSRConfs = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1))
tmnxSRObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2))
tmnxSRNotifyPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 3))
tmnxESSMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 2))
tmnxESSConfs = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 2, 1))
tmnxESSObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 2, 2))
tmnxESSNotifyPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 2, 3))
alcatelCommonMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 3))
alcatelConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 3, 1))
alcatelObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 3, 2))
alcatelNotifyPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 3, 3))
tmnxAgentCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 4))
tmnx7750AgentCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 4, 1))
tmnx7450AgentCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 4, 2))
tmnx7710AgentCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 4, 3))
tmnxProductCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 5))
tmnx7750Capability = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 5, 1))
tmnx7750V3v0 = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 5, 1, 1))
tmnx7750V4v0 = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 5, 1, 2))
tmnx7750V5v0 = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 5, 1, 3))
tmnx7750V6v0 = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 5, 1, 4))
tmnx7450Capability = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 5, 2))
tmnx7450V3v0 = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 5, 2, 1))
tmnx7450V4v0 = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 5, 2, 2))
tmnx7450V5v0 = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 5, 2, 3))
tmnx7450V6v0 = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 5, 2, 4))
tmnx7710Capability = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 5, 3))
tmnx7710V3v0 = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 5, 3, 1))
tmnx7710V4v0 = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 5, 3, 2))
tmnx7710V5v0 = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 5, 3, 3))
tmnx7710V6v0 = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 5, 3, 4))
mibBuilder.exportSymbols("ALCATEL-IND1-TIMETRA-GLOBAL-MIB", timetraSRMIBModules=timetraSRMIBModules, timetra7750CapModule=timetra7750CapModule, tmnxModelESS6vReg=tmnxModelESS6vReg, tmnx7750V3v0=tmnx7750V3v0, tmnxModelESS7Reg=tmnxModelESS7Reg, tmnxSRConfs=tmnxSRConfs, tmnxModelSR1Reg=tmnxModelSR1Reg, tmnx7750Capability=tmnx7750Capability, tmnxSRObjs=tmnxSRObjs, alcatelCommonMIBModules=alcatelCommonMIBModules, tmnxModelSR7Reg=tmnxModelSR7Reg, tmnx7710V3v0=tmnx7710V3v0, tmnx7710Capability=tmnx7710Capability, tmnx7450V6v0=tmnx7450V6v0, PYSNMP_MODULE_ID=timetraGlobalMIBModule, timetra7450CapModule=timetra7450CapModule, tmnxModelSR4Reg=tmnxModelSR4Reg, tmnxModelESS12Reg=tmnxModelESS12Reg, tmnxModelESS6Reg=tmnxModelESS6Reg, tmnxSRNotifyPrefix=tmnxSRNotifyPrefix, tmnxModelSR12Reg=tmnxModelSR12Reg, tmnxESSConfs=tmnxESSConfs, tmnxAgentCapability=tmnxAgentCapability, tmnx7750V5v0=tmnx7750V5v0, tmnx7710V4v0=tmnx7710V4v0, tmnx7450AgentCapability=tmnx7450AgentCapability, timetraCapabilityModule=timetraCapabilityModule, tmnx7710V5v0=tmnx7710V5v0, alcatelCommonMIB=alcatelCommonMIB, tmnx7750V4v0=tmnx7750V4v0, tmnxESSNotifyPrefix=tmnxESSNotifyPrefix, tmnxModelSR6Reg=tmnxModelSR6Reg, tmnxESSObjs=tmnxESSObjs, timetraModules=timetraModules, timetraGlobalMIBModule=timetraGlobalMIBModule, timetraProducts=timetraProducts, tmnxModel7710SRc4Reg=tmnxModel7710SRc4Reg, tmnxESSMIB=tmnxESSMIB, tmnx7450V5v0=tmnx7450V5v0, tmnx7450V3v0=tmnx7450V3v0, timetra=timetra, alcatelNotifyPrefix=alcatelNotifyPrefix, tmnx7450Capability=tmnx7450Capability, alcatelConformance=alcatelConformance, tmnx7750V6v0=tmnx7750V6v0, tmnxModelESS4Reg=tmnxModelESS4Reg, tmnx7710V6v0=tmnx7710V6v0, tmnx7750AgentCapability=tmnx7750AgentCapability, tmnxProductCapability=tmnxProductCapability, timetraGeneric=timetraGeneric, alcatel7710ServiceRouters=alcatel7710ServiceRouters, tmnxModelESS1Reg=tmnxModelESS1Reg, timetraServiceRouters=timetraServiceRouters, tmnxModel7710SRc12Reg=tmnxModel7710SRc12Reg, tmnxSRMIB=tmnxSRMIB, tmnx7710AgentCapability=tmnx7710AgentCapability, tmnx7450V4v0=tmnx7450V4v0, timetraReg=timetraReg, timetraServiceSwitches=timetraServiceSwitches, timetra7710CapModule=timetra7710CapModule, alcatelObjects=alcatelObjects)
