#
# PySNMP MIB module PAN-GLOBAL-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PAN-GLOBAL-TC
# Produced by pysmi-0.3.4 at Wed May  1 14:36:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
panModules, = mibBuilder.importSymbols("PAN-GLOBAL-REG", "panModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, NotificationType, ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, MibIdentifier, Counter64, ObjectIdentity, IpAddress, Bits, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "NotificationType", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "MibIdentifier", "Counter64", "ObjectIdentity", "IpAddress", "Bits", "TimeTicks", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
panGlobalTcModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 25461, 1, 1, 2))
panGlobalTcModule.setRevisions(('2011-02-09 16:10',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: panGlobalTcModule.setRevisionsDescriptions((' Rev 1.0 Initial version of MIB module PAN-GLOBAL-TC.',))
if mibBuilder.loadTexts: panGlobalTcModule.setLastUpdated('201106271040Z')
if mibBuilder.loadTexts: panGlobalTcModule.setOrganization('Palo Alto Networks')
if mibBuilder.loadTexts: panGlobalTcModule.setContactInfo(' Customer Support Palo Alto Networks 4401 Great America Pkwy Santa Clara, CA 95054-1211 +1 866-898-9087 support at paloaltonetworks dot com')
if mibBuilder.loadTexts: panGlobalTcModule.setDescription(" A MIB module containing textual conventions for Palo Alto Networks' enterprise MIB modules. These textual conventions are used across all Palo Alto products.")
class TcAppaname(TextualConvention, OctetString):
    description = " Represents the name of an application. This has all the restrictions of the DisplayString textual convention with the following additional ones: - Only the following characters/character ranges are allowed: 0-9 A-Z a-z :./#$&_-+()' <space> Any object defined using this syntax may not exceed 64 characters in length."
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class TcChassisType(TextualConvention, OctetString):
    description = ' Enumerates all possible chassis types for Palo Alto devices.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

mibBuilder.exportSymbols("PAN-GLOBAL-TC", panGlobalTcModule=panGlobalTcModule, TcChassisType=TcChassisType, TcAppaname=TcAppaname, PYSNMP_MODULE_ID=panGlobalTcModule)
