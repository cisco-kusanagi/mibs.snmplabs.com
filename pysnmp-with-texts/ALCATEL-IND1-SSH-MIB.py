#
# PySNMP MIB module ALCATEL-IND1-SSH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALCATEL-IND1-SSH-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:19:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
softentIND1Ssh, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "softentIND1Ssh")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ObjectIdentity, iso, ModuleIdentity, TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Integer32, Unsigned32, Counter64, Bits, Counter32, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "iso", "ModuleIdentity", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Integer32", "Unsigned32", "Counter64", "Bits", "Counter32", "Gauge32", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
alcatelIND1SshMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 39, 1))
alcatelIND1SshMIB.setRevisions(('2007-04-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: alcatelIND1SshMIB.setRevisionsDescriptions(('The latest version of this MIB Module.',))
if mibBuilder.loadTexts: alcatelIND1SshMIB.setLastUpdated('200704030000Z')
if mibBuilder.loadTexts: alcatelIND1SshMIB.setOrganization('Alcatel-Lucent')
if mibBuilder.loadTexts: alcatelIND1SshMIB.setContactInfo('Please consult with Customer Service to ensure the most appropriate version of this document is used with the products in question: Alcatel-Lucent, Enterprise Solutions Division (Formerly Alcatel Internetworking, Incorporated) 26801 West Agoura Road Agoura Hills, CA 91301-5122 United States Of America Telephone: North America +1 800 995 2696 Latin America +1 877 919 9526 Europe +31 23 556 0100 Asia +65 394 7933 All Other +1 818 878 4507 Electronic Mail: support@ind.alcatel.com World Wide Web: http://alcatel-lucent.com/wps/portal/enterprise File Transfer Protocol: ftp://ftp.ind.alcatel.com/pub/products/mibs')
if mibBuilder.loadTexts: alcatelIND1SshMIB.setDescription('This module describes an authoritative enterprise-specific SSH Management Information Base (MIB): For the Birds Of Prey Product Line SSH Subsystem. The right to make changes in specification and other information contained in this document without prior notice is reserved. No liability shall be assumed for any incidental, indirect, special, or consequential damages whatsoever arising from or related to this document or the information contained herein. Vendors, end-users, and other interested parties are granted non-exclusive license to use this specification in connection with management of the products for which it is intended to be used. Copyright (C) 1995-2007 Alcatel-Lucent ALL RIGHTS RESERVED WORLDWIDE')
alcatelIND1SshMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 39, 1, 1))
if mibBuilder.loadTexts: alcatelIND1SshMIBObjects.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1SshMIBObjects.setDescription('Branch For SNMP Agent Subsystem Managed Objects.')
alcatelIND1SshMIBConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 39, 1, 2))
if mibBuilder.loadTexts: alcatelIND1SshMIBConformance.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1SshMIBConformance.setDescription('Branch For SSH Subsystem Conformance Information.')
alcatelIND1SshMIBGroups = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 39, 1, 2, 1))
if mibBuilder.loadTexts: alcatelIND1SshMIBGroups.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1SshMIBGroups.setDescription('Branch For SSH Subsystem Units Of Conformance.')
alcatelIND1SshMIBCompliances = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 39, 1, 2, 2))
if mibBuilder.loadTexts: alcatelIND1SshMIBCompliances.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1SshMIBCompliances.setDescription('Branch For SSH Subsystem Compliance Statements.')
alaSshAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 39, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaSshAdminStatus.setStatus('current')
if mibBuilder.loadTexts: alaSshAdminStatus.setDescription('Indicates whether the SSH service is enabled on the switch.')
alaScpSftpAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 39, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaScpSftpAdminStatus.setStatus('current')
if mibBuilder.loadTexts: alaScpSftpAdminStatus.setDescription('Indicates whether the SCP/SFTP service is enabled on the switch.')
alaSshPubKeyEnforceAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 39, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaSshPubKeyEnforceAdminStatus.setStatus('current')
if mibBuilder.loadTexts: alaSshPubKeyEnforceAdminStatus.setDescription('Indicates whether the Public Key Authentication is enforced on the switch.')
alcatelIND1SshMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 39, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-SSH-MIB", "alaSshConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alcatelIND1SshMIBCompliance = alcatelIND1SshMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1SshMIBCompliance.setDescription('Compliance statement for SSH Subsystem.')
alaSshConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 39, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-SSH-MIB", "alaSshAdminStatus"), ("ALCATEL-IND1-SSH-MIB", "alaScpSftpAdminStatus"), ("ALCATEL-IND1-SSH-MIB", "alaSshPubKeyEnforceAdminStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaSshConfigGroup = alaSshConfigGroup.setStatus('current')
if mibBuilder.loadTexts: alaSshConfigGroup.setDescription('Collection of objects for SSH configuration.')
mibBuilder.exportSymbols("ALCATEL-IND1-SSH-MIB", alaSshPubKeyEnforceAdminStatus=alaSshPubKeyEnforceAdminStatus, alcatelIND1SshMIBCompliance=alcatelIND1SshMIBCompliance, alaSshConfigGroup=alaSshConfigGroup, alcatelIND1SshMIBCompliances=alcatelIND1SshMIBCompliances, alcatelIND1SshMIBGroups=alcatelIND1SshMIBGroups, alcatelIND1SshMIBConformance=alcatelIND1SshMIBConformance, PYSNMP_MODULE_ID=alcatelIND1SshMIB, alaScpSftpAdminStatus=alaScpSftpAdminStatus, alcatelIND1SshMIB=alcatelIND1SshMIB, alcatelIND1SshMIBObjects=alcatelIND1SshMIBObjects, alaSshAdminStatus=alaSshAdminStatus)
