#
# PySNMP MIB module BYTESPHERE-TRAPMGR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BYTESPHERE-TRAPMGR-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:42:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
bytesphereMgmt, = mibBuilder.importSymbols("BYTESPHERE-SMI", "bytesphereMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, Unsigned32, IpAddress, ObjectIdentity, MibIdentifier, Gauge32, Counter32, Integer32, ModuleIdentity, NotificationType, Counter64, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "Unsigned32", "IpAddress", "ObjectIdentity", "MibIdentifier", "Gauge32", "Counter32", "Integer32", "ModuleIdentity", "NotificationType", "Counter64", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bytesphereTrapMgrMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 7013, 1, 2))
bytesphereTrapMgrMib.setRevisions(('2007-10-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bytesphereTrapMgrMib.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: bytesphereTrapMgrMib.setLastUpdated('200710050000Z')
if mibBuilder.loadTexts: bytesphereTrapMgrMib.setOrganization('ByteSphere Technologies LLC')
if mibBuilder.loadTexts: bytesphereTrapMgrMib.setContactInfo(' ByteSphere Technologies LLC Postal: 955 Mass Ave #141 Cambridge, MA 02139 USA E-mail: bscustsupt@bytesphere.com')
if mibBuilder.loadTexts: bytesphereTrapMgrMib.setDescription('The MIB module to describe OIDs and behavior for the Trap Manager system.')
bytesphereTrapMgrObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 7013, 1, 2, 1))
trapMgrSourceHost = MibScalar((1, 3, 6, 1, 4, 1, 7013, 1, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapMgrSourceHost.setStatus('current')
if mibBuilder.loadTexts: trapMgrSourceHost.setDescription('The IP Address of the forwarding Trap Manager Host. This object is added into the varbinds when traps are forwarded from Trap Manager to another host.')
mibBuilder.exportSymbols("BYTESPHERE-TRAPMGR-MIB", trapMgrSourceHost=trapMgrSourceHost, bytesphereTrapMgrMib=bytesphereTrapMgrMib, PYSNMP_MODULE_ID=bytesphereTrapMgrMib, bytesphereTrapMgrObjects=bytesphereTrapMgrObjects)
