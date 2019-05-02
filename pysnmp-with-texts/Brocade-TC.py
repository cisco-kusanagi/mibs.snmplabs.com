#
# PySNMP MIB module Brocade-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Brocade-TC
# Produced by pysmi-0.3.4 at Wed May  1 11:36:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
bcsiModules, = mibBuilder.importSymbols("Brocade-REG-MIB", "bcsiModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Unsigned32, Integer32, NotificationType, Counter32, iso, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, Counter64, Gauge32, ModuleIdentity, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Unsigned32", "Integer32", "NotificationType", "Counter32", "iso", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "Counter64", "Gauge32", "ModuleIdentity", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bcsiModuleTC = ModuleIdentity((1, 3, 6, 1, 4, 1, 1588, 3, 1, 2))
bcsiModuleTC.setRevisions(('2003-01-13 14:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bcsiModuleTC.setRevisionsDescriptions(('The initial version of this module.',))
if mibBuilder.loadTexts: bcsiModuleTC.setLastUpdated('200301131430Z')
if mibBuilder.loadTexts: bcsiModuleTC.setOrganization('Brocade Communications Systems, Inc.,')
if mibBuilder.loadTexts: bcsiModuleTC.setContactInfo('Customer Support Group Brocade Communications Systems, 1745 Technology Drive, San Jose, CA 95110 U.S.A Tel: +1-408-392-6061 Fax: +1-408-392-6656 Email: support@Brocade.COM WEB: www.brocade.com')
if mibBuilder.loadTexts: bcsiModuleTC.setDescription('The MIB module contains all shared textual conventions for Brocade specific MIBs. Copyright (c) 1996-2002 Brocade Communications Systems, Inc. All rights reserved.')
class FcWwn(TextualConvention, OctetString):
    description = "The World Wide Name (WWN) of Brocade's specific products and ports."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class SwDomainIndex(TextualConvention, Integer32):
    description = 'The Fibre Channel domain ID of the switch.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 239)

class SwNbIndex(TextualConvention, Integer32):
    description = 'Index of the neighbour ISL entry.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2048)

class SwSensorIndex(TextualConvention, Integer32):
    description = 'Index of the Sensor entry.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 1024)

class SwPortIndex(TextualConvention, Integer32):
    description = 'Index of the Port start from 1 upto Maximum number of ports of the Brocade Switch.'
    status = 'current'

class SwTrunkMaster(TextualConvention, Integer32):
    description = 'Index of the Trunk Master start from 1 upto Maximum number of trunk groups of Brocade Switch.'
    status = 'current'

mibBuilder.exportSymbols("Brocade-TC", SwTrunkMaster=SwTrunkMaster, bcsiModuleTC=bcsiModuleTC, PYSNMP_MODULE_ID=bcsiModuleTC, SwDomainIndex=SwDomainIndex, FcWwn=FcWwn, SwSensorIndex=SwSensorIndex, SwPortIndex=SwPortIndex, SwNbIndex=SwNbIndex)
