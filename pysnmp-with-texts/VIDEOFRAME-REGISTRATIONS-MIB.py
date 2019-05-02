#
# PySNMP MIB module VIDEOFRAME-REGISTRATIONS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/VIDEOFRAME-REGISTRATIONS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:34:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, ObjectIdentity, NotificationType, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier, iso, Counter64, Integer32, IpAddress, ModuleIdentity, Unsigned32, enterprises, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "NotificationType", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier", "iso", "Counter64", "Integer32", "IpAddress", "ModuleIdentity", "Unsigned32", "enterprises", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
videoframe = ObjectIdentity((1, 3, 6, 1, 4, 1, 4596))
if mibBuilder.loadTexts: videoframe.setStatus('current')
if mibBuilder.loadTexts: videoframe.setDescription('Enterprise name space assigned to Videoframe Systems by IANA.')
vfGeneric = ObjectIdentity((1, 3, 6, 1, 4, 1, 4596, 3))
if mibBuilder.loadTexts: vfGeneric.setStatus('current')
if mibBuilder.loadTexts: vfGeneric.setDescription('Name space for object definitions common among Videoframe managed devices.')
vfProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 4596, 4))
if mibBuilder.loadTexts: vfProducts.setStatus('current')
if mibBuilder.loadTexts: vfProducts.setDescription('Name space for object definitions specific to particular Videoframe managed device types.')
vfExperimental = ObjectIdentity((1, 3, 6, 1, 4, 1, 4596, 5))
if mibBuilder.loadTexts: vfExperimental.setStatus('current')
if mibBuilder.loadTexts: vfExperimental.setDescription('vfExperimental provides a root OID from which experimental MIBs are temporarily based. MIBs that are placed here are Videoframe works-in-progress and have not been assigned a permanent OID by Videoframe, typically because the MIB was not ready for deployment.')
vfRegistrations = ObjectIdentity((1, 3, 6, 1, 4, 1, 4596, 6))
if mibBuilder.loadTexts: vfRegistrations.setStatus('current')
if mibBuilder.loadTexts: vfRegistrations.setDescription("Name space for Videoframe's authoritatively assigned registrations and MIB modules.")
vfMIBModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 4596, 6, 1))
if mibBuilder.loadTexts: vfMIBModules.setStatus('current')
if mibBuilder.loadTexts: vfMIBModules.setDescription('Name space for Registration of MIB modules defined by videoframe systems.')
vfReg = ModuleIdentity((1, 3, 6, 1, 4, 1, 4596, 6, 1, 1))
vfReg.setRevisions(('1901-01-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: vfReg.setRevisionsDescriptions(('First release.',))
if mibBuilder.loadTexts: vfReg.setLastUpdated('0108270000Z')
if mibBuilder.loadTexts: vfReg.setOrganization('Videoframe Systems')
if mibBuilder.loadTexts: vfReg.setContactInfo('Videoframe Systems P.O. Box 1991, Grass Valley, CA 95945, USA. +1 (530) 477-2000 http://www.videoframesystems.com')
if mibBuilder.loadTexts: vfReg.setDescription('This MIB module describes the upper level OID registrations for the Videoframe enterprise naming space. This module will be extended, or modified as required. Videoframe Systems reserves the right to make changes in specification and other information contained in this document without prior notice. The reader should consult Videoframe Systems to determine whether any such changes have been made. In no event shall Videoframe Systems be liable for any incidental, indirect, special, or consequential damages whatsoever (including but not limited to lost profits) arising out of or related to this document or the information contained in it. Videoframe Systems grants vendors, end users, and other interested parties a non-exclusive license to use this specification in connection with the management of Videoframe Systems products. Copyright 2001 Videoframe, Inc.')
vfProductsReg = ObjectIdentity((1, 3, 6, 1, 4, 1, 4596, 6, 2))
if mibBuilder.loadTexts: vfProductsReg.setStatus('current')
if mibBuilder.loadTexts: vfProductsReg.setDescription('Name space for Registration of products offered by videoframe systems.')
vfProductsRMCReg = ObjectIdentity((1, 3, 6, 1, 4, 1, 4596, 6, 2, 1))
if mibBuilder.loadTexts: vfProductsRMCReg.setStatus('current')
if mibBuilder.loadTexts: vfProductsRMCReg.setDescription('VF100 RTU Monitoring Controller.')
vfProductsSAPSCtlReg = ObjectIdentity((1, 3, 6, 1, 4, 1, 4596, 6, 2, 2))
if mibBuilder.loadTexts: vfProductsSAPSCtlReg.setStatus('current')
if mibBuilder.loadTexts: vfProductsSAPSCtlReg.setDescription('VF100 SAPS Controller.')
vfProductsGPIAgentReg = ObjectIdentity((1, 3, 6, 1, 4, 1, 4596, 6, 2, 3))
if mibBuilder.loadTexts: vfProductsGPIAgentReg.setStatus('current')
if mibBuilder.loadTexts: vfProductsGPIAgentReg.setDescription('VF100 GPI SNMP Agent.')
mibBuilder.exportSymbols("VIDEOFRAME-REGISTRATIONS-MIB", vfProducts=vfProducts, vfProductsGPIAgentReg=vfProductsGPIAgentReg, vfProductsReg=vfProductsReg, vfProductsRMCReg=vfProductsRMCReg, vfRegistrations=vfRegistrations, vfExperimental=vfExperimental, vfReg=vfReg, vfProductsSAPSCtlReg=vfProductsSAPSCtlReg, videoframe=videoframe, PYSNMP_MODULE_ID=vfReg, vfGeneric=vfGeneric, vfMIBModules=vfMIBModules)
